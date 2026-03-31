from rest_framework import permissions, serializers, viewsets

from .models import DataImport


class DataImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataImport
        fields = "__all__"


class DataImportViewSet(viewsets.ModelViewSet):
    serializer_class = DataImportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DataImport.objects.filter(user=self.request.user)
