from rest_framework import permissions, serializers, viewsets

from .models import MLModelLog


class MLModelLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModelLog
        fields = "__all__"


class MLModelLogViewSet(viewsets.ModelViewSet):
    serializer_class = MLModelLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MLModelLog.objects.filter(user=self.request.user)
