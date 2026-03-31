from rest_framework import permissions, serializers, viewsets

from .models import UserSetting


class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = "__all__"


class UserSettingViewSet(viewsets.ModelViewSet):
    serializer_class = UserSettingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserSetting.objects.filter(user=self.request.user)
