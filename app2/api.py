from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models as app2_models
from . import serializers as app2_serializers


class ItemRateModelViewSet(ModelViewSet):
    queryset = app2_models.ItemRate.objects.all()
    serializer_class = app2_serializers.ItemRateSerializer

    @action(methods=['post'], detail=False, url_path='multiple/create1')
    def multiple_create1(self, request, *args, **kwargs):
        for data in request.data:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        return super().list(self, request, *args, **kwargs)

    @action(methods=['post'], detail=False, url_path='multiple/create2')
    def multiple_create2(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)
