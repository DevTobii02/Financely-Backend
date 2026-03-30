from django.db import models

# Create your models here.
from users.models import CustomUser

class DataImport(models.Model):
    """
    Tracks financial data files uploaded by users.
    Supports AI processing, analytics, and versioning.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Owner of the uploaded data

    file = models.FileField(upload_to='user_data/%Y/%m/%d/')
    # Actual uploaded file stored in media folder

    file_name = models.CharField(max_length=100)
    # Optional: store original name for display

    file_type = models.CharField(max_length=10)
    # CSV, XLSX, etc.

    file_size = models.PositiveIntegerField(blank=True, null=True)
    # Store file size in bytes for analytics / validation

    description = models.TextField(blank=True, null=True)
    # Optional description about file content

    processed = models.BooleanField(default=False)
    # Whether AI has processed the file

    processing_notes = models.TextField(blank=True, null=True)
    # Optional notes about processing (errors, AI recommendations)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Timestamps for tracking uploads and processing updates

    version = models.PositiveIntegerField(default=1)
    # Allows tracking multiple uploads of the same type

    def __str__(self):
        return f"{self.file_name} ({self.user.username})"