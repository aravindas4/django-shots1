from rest_framework.routers import SimpleRouter

from . import api as app2_api

router = SimpleRouter()

router.register(r'item/rate', app2_api.ItemRateModelViewSet, basename='app2-item-rate')

urlpatterns = router.urls
