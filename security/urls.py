from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TwoFactorAuthViewSet

router = DefaultRouter()
router.register(r"two-factor-auth", TwoFactorAuthViewSet, basename="two-factor-auth")

urlpatterns = [
    path("", include(router.urls)),
]
