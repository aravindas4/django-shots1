from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.exceptions import APIException


class APIValidationError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _('Invalid Request')
    default_code = 'detail'
