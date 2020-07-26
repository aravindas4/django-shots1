from rest_framework.routers import SimpleRouter

from .api import LoanApplicationViewSet

router = SimpleRouter()

router.register(r'loan/application', LoanApplicationViewSet,
                basename='account-loan-application')

urlpatterns = router.urls
