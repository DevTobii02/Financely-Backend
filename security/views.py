from rest_framework import permissions, serializers, viewsets

from .models import TwoFactorAuth


class TwoFactorAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoFactorAuth
        fields = "__all__"


class TwoFactorAuthViewSet(viewsets.ModelViewSet):
    serializer_class = TwoFactorAuthSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TwoFactorAuth.objects.filter(user=self.request.user)
