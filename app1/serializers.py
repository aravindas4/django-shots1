from rest_framework import serializers
from .models import Account, LoanApplication


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class LoanApplicationSerializer(serializers.ModelSerializer):
    approved_amount = serializers.IntegerField(
        source='account.approved_amount')
    reason = serializers.CharField(source='account.reason')

    class Meta:
        model = LoanApplication
        exclude = ('account',)

    def update(self, instance, validated_data):
        account_data = validated_data.pop('account', None)
        if account_data:
            account_serializer = AccountSerializer(
                instance.account, data=account_data, partial=True)
            account_serializer.is_valid(raise_exception=True)
            account_serializer.save()

        return super().update(instance, validated_data)
