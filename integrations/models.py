from django.db import models
from users.models import CustomUser

# Create your models here.

class Integration(models.Model):
    """
    Represents a third-party service integration for a user.
    Examples: Bank account, PayPal, Stripe, accounting software, or other APIs.
    """

    SERVICE_CHOICES = (
        ('bank', 'Bank'),
        ('payment', 'Payment Provider'),
        ('accounting', 'Accounting Software'),
        ('crypto', 'Cryptocurrency Exchange'),
        ('other', 'Other'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Owner of the integration

    name = models.CharField(max_length=100)
    # Name of the service (e.g., "GTBank", "PayPal")

    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='other')
    # Type of service

    api_key = models.CharField(max_length=255, blank=True, null=True)
    api_secret = models.CharField(max_length=255, blank=True, null=True)
    # Store credentials securely (consider encrypting in production)

    access_token = models.CharField(max_length=255, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    token_expiry = models.DateTimeField(blank=True, null=True)
    # Tokens and expiry for services requiring OAuth or API authentication

    is_active = models.BooleanField(default=True)
    # Whether the integration is currently active

    last_synced_at = models.DateTimeField(blank=True, null=True)
    # Last time data was successfully synced from this integration

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Track when the integration was added and last updated

    notes = models.TextField(blank=True, null=True)
    # Optional notes, e.g., "Requires 2FA"

    class Meta:
        unique_together = ('user', 'name', 'service_type')
        # Prevent duplicate integration for the same user and service

    def __str__(self):
        return f"{self.name} ({self.user.username})"