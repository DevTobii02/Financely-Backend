from django.db import models
from users.models import CustomUser

# Create your models here.

class Goal(models.Model):
    """
    Tracks financial goals set by users.
    Supports progress tracking, AI recommendations, and analytics.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Owner of the goal

    name = models.CharField(max_length=100)
    # Name/title of the goal

    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    # The amount the user wants to save

    saved_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Current progress

    deadline = models.DateField()
    # Target date to achieve the goal

    goal_type = models.CharField(
        max_length=20,
        choices=(('short_term', 'Short Term'), ('long_term', 'Long Term'), ('investment', 'Investment')),
        default='short_term'
    )
    # Categorize goal type for analytics and AI recommendations

    currency = models.CharField(max_length=10, default='NGN')
    # Currency of the goal amount

    description = models.TextField(blank=True, null=True)
    # Optional notes about the goal

    is_active = models.BooleanField(default=True)
    # Track active vs archived/completed goals

    achieved = models.BooleanField(default=False)
    # Has the goal been achieved?

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Track creation and updates for AI analytics

    class Meta:
        unique_together = ('user', 'name')
        # Prevent duplicate goal names for the same user

    def __str__(self):
        return f"{self.name} ({self.user.username})"