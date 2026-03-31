from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DataImportViewSet

router = DefaultRouter()
router.register(r"data-imports", DataImportViewSet, basename="data-import")

urlpatterns = [
    path("", include(router.urls)),
]
