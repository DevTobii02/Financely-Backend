from django.db import models
from users.models import CustomUser

# Create your models here.

class TwoFactorAuth(models.Model):
    """
    Handles two-factor authentication (2FA) for users.
    Supports multiple 2FA methods, audit timestamps, and recovery options.
    """

    METHOD_CHOICES = (
        ('app', 'Authenticator App'),
        ('sms', 'SMS'),
        ('email', 'Email'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Owner of the 2FA setup

    enabled = models.BooleanField(default=False)
    # Is 2FA currently enabled?

    method = models.CharField(max_length=10, choices=METHOD_CHOICES, default='app')
    # Type of 2FA method

    secret_key = models.CharField(max_length=100, blank=True, null=True)
    # Secret key for app-based 2FA

    backup_codes = models.JSONField(blank=True, null=True)
    # Optional: store encrypted backup codes for recovery

    last_verified_at = models.DateTimeField(blank=True, null=True)
    # Last time the user successfully verified 2FA

    is_active = models.BooleanField(default=True)
    # Whether this 2FA record is currently active

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Timestamps for auditing and consistency

    class Meta:
        unique_together = ('user', 'method')
        # Prevent duplicate 2FA method setups per user

    def __str__(self):
        return f"2FA ({self.method}) for {self.user.username} - {'Enabled' if self.enabled else 'Disabled'}"