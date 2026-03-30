from django.db import models

# Create your models here.
from users.models import CustomUser
class UserSetting(models.Model):
    """
    Flexible key-value store for user-specific settings.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # The user this setting belongs to

    key = models.CharField(max_length=100)
    # Setting name (e.g., 'dark_mode', 'currency')

    value = models.JSONField()
    # Flexible value (can store bool, string, dict, etc.)

    updated_at = models.DateTimeField(auto_now=True)
    # Automatically updates whenever setting changes

    class Meta:
        unique_together = ('user', 'key')
        # Prevent duplicate keys per user

    def __str__(self):
        return f"{self.user.username} - {self.key}"