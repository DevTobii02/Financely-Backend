from django.db import models
from users.models import CustomUser
from categories.models import Category

# Create your models here.

class SpendingSummary(models.Model):
    """
    Stores monthly spending summary per category for each user.
    Used for analytics, reports, and AI insights.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # The user this summary belongs to

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Category being summarized (e.g., Food, Transport)

    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Total spending in that category for the month

    month = models.DateField()
    # Represents the month (use first day of month convention, e.g., 2026-03-01)

    created_at = models.DateTimeField(auto_now_add=True)
    # When this summary was generated

    class Meta:
        unique_together = ('user', 'category', 'month')
        # Prevent duplicate summaries for same user/category/month

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.month}"