from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SpendingSummaryViewSet

router = DefaultRouter()
router.register(r"spending-summaries", SpendingSummaryViewSet, basename="spending-summary")

urlpatterns = [
    path("", include(router.urls)),
]
