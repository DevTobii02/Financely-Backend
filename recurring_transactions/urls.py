from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RecurringTransactionViewSet

router = DefaultRouter()
router.register(r"recurring-transactions", RecurringTransactionViewSet, basename="recurring-transaction")

urlpatterns = [
    path("", include(router.urls)),
]
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RecurringTransactionViewSet

router = DefaultRouter()
router.register(r"recurring-transactions", RecurringTransactionViewSet, basename="recurring-transaction")

urlpatterns = [
    path("", include(router.urls)),
]
