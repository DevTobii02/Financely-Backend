from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BillPaymentViewSet, BillViewSet

router = DefaultRouter()
router.register(r"bills", BillViewSet, basename="bill")
router.register(r"bill-payments", BillPaymentViewSet, basename="bill-payment")

urlpatterns = [
    path("", include(router.urls)),
]
