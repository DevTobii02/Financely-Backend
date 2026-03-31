from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ChatMessageViewSet

router = DefaultRouter()
router.register(r"chat-messages", ChatMessageViewSet, basename="chat-message")

urlpatterns = [
    path("", include(router.urls)),
]
