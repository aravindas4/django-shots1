from rest_framework import serializers

from . import models as app2_models


class ItemRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = app2_models.ItemRate
        fields = '__all__'
