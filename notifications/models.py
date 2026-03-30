from django.db import models
from users.models import CustomUser
from budgets.models import Budget
from goals.models import Goal

# Create your models here.

class Notification(models.Model):
    """
    Stores notifications sent to the user.
    Supports context linking (transactions, budgets, goals), priority, and read/unread tracking.
    """

    NOTIF_TYPE = (
        ('reminder', 'Reminder'),
        ('alert', 'Alert'),
        ('info', 'Information'),
        ('warning', 'Warning'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Owner of the notification

    type = models.CharField(max_length=10, choices=NOTIF_TYPE)
    # Type of notification (reminder, alert, etc.)

    message = models.TextField()
    # Content of the notification

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    # Optional: priority level

    related_transaction = models.ForeignKey('transactions.Transaction', on_delete=models.SET_NULL, blank=True, null=True, related_name='related_notifications')
    related_budget = models.ForeignKey(Budget, on_delete=models.SET_NULL, blank=True, null=True)
    related_goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, blank=True, null=True)
    # Optional context for AI-driven notifications

    read = models.BooleanField(default=False)
    # Has the user read this notification?

    is_active = models.BooleanField(default=True)
    # Can deactivate outdated notifications

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Track creation and last update

    source = models.CharField(max_length=50, blank=True, null=True)
    # Optional: 'AI', 'System', 'User', etc.

    class Meta:
        ordering = ['-created_at']
        # Most recent notifications appear first

    def __str__(self):
        return f"{self.type} for {self.user.username}: {self.message[:30]}"