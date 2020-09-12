import os
import uuid

from django.conf import settings
from django.db import models

from rest_framework import serializers

from utils import s3
from utils.serializers import BaseSerializer
from utils.exceptions import APIValidationError


class Document(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class File(models.Model):
    path = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Invoice(Document):
    pass


class InvoiceFile(File):
    invoice = models.ForeignKey(Invoice, related_name='files',
                                on_delete=models.CASCADE)


# 2
class Product(models.Model):
    name = models.CharField(max_length=255)

    def copy_seller_invoice_files(self, data):
        result = []

        for index, file in enumerate(data):
            file_name = f'{self.id}_buyer_invoice_{index}_{str(uuid.uuid4()).upper()[:8]}.pdf'
            new_path = f'/tmp/{file_name}'
            aws_path = f'{self.name}/{file_name}'
            s3.download_object(
                new_path,
                settings.AWS_STORAGE_BUCKET_NAME,
                file['document'])

            try:
                s3.upload_object(
                    new_path,
                    settings.AWS_STORAGE_BUCKET_NAME,
                    aws_path)
            except Exception as e:
                raise APIValidationError(detail='Unable to Upload Files')

            result.append({'document': aws_path})
            os.remove(new_path)
        return result


# seller
class SellerInvoice(Invoice):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)


class SellerInvoiceFile(File):
    seller_invoice = models.ForeignKey(SellerInvoice, related_name='seller_files',
                                on_delete=models.CASCADE)


# buyer
class BuyerInvoice(Invoice):
    pass


class BuyerInvoiceFile(File):
    invoice = models.ForeignKey(BuyerInvoice, related_name='buyer_files',
                                on_delete=models.CASCADE)


class BuyerInvoiceFileSerializer(BaseSerializer):

    class Meta:
        model = BuyerInvoiceFile
        fields = '__all__'
        extra_kwargs = {
            'invoice': {
                'write_only': True,
                'required': False
            }
        }


class SellerInvoiceFileSerializer(BaseSerializer):

    class Meta:
        model = SellerInvoiceFile
        fields = '__all__'
        extra_kwargs = {
            'invoice': {
                'write_only': True,
                'required': False
            }
        }


class BuyerInvoiceSerializer(BaseSerializer):
    is_same_as_seller = serializers.BooleanField(write_only=True,
                                                   default=False)
    buyer_files = BuyerInvoiceFileSerializer(many=True)

    class Meta:
        model = BuyerInvoice
        fields = '__all__'

    def create(self, validated_data):
        product = validated_data['product']

        if validated_data['is_same_as_seller']:
            validated_data['name'] = product.sellerinvoice.name
            file_data = BuyerInvoiceFileSerializer(
                data=SellerInvoiceFileSerializer(
                    product.sellerinvoice.seller_files.all(),
                    fields=["path"], many=True).data,
                many=True)
            file_data.is_valid(raise_exception=True)
            # validated_data['buyer_files'] = file_data.data
            self.initial_data.update({
                'buyer_files': product.copy_seller_invoice_files(
                    list(file_data.data))
            })

        return super().create(validated_data)
