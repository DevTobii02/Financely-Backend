from rest_framework import permissions, serializers, viewsets

from .models import SpendingSummary


class SpendingSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingSummary
        fields = "__all__"


class SpendingSummaryViewSet(viewsets.ModelViewSet):
    serializer_class = SpendingSummarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SpendingSummary.objects.filter(user=self.request.user)
