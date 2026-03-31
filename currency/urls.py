from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CurrencyViewSet, ExchangeRateViewSet

router = DefaultRouter()
router.register(r"currencies", CurrencyViewSet, basename="currency")
router.register(r"exchange-rates", ExchangeRateViewSet, basename="exchange-rate")

urlpatterns = [
    path("", include(router.urls)),
]
