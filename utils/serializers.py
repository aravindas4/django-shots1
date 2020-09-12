from drf_writable_nested import WritableNestedModelSerializer
from rest_flex_fields.serializers import FlexFieldsSerializerMixin


class BaseSerializer(FlexFieldsSerializerMixin, WritableNestedModelSerializer):
    pass
