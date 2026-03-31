from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserSettingViewSet

router = DefaultRouter()
router.register(r"user-settings", UserSettingViewSet, basename="user-setting")

urlpatterns = [
    path("", include(router.urls)),
]
