from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MLModelLogViewSet

router = DefaultRouter()
router.register(r"ml-model-logs", MLModelLogViewSet, basename="ml-model-log")

urlpatterns = [
    path("", include(router.urls)),
]
