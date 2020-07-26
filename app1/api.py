from rest_framework.viewsets import ModelViewSet
from .models import LoanApplication
from .serializers import LoanApplicationSerializer


class LoanApplicationViewSet(ModelViewSet):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer
