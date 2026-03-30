from django.db import models

# Create your models here.
from users.models import CustomUser
from categories.models import Category

class Budget(models.Model):
    """
    User-defined budget for a category during a specific period.
    Tracks spending limits, active status, and allows integration with notifications and AI insights.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # The owner of the budget

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Category this budget applies to (e.g., Food, Transport)

    limit = models.DecimalField(max_digits=12, decimal_places=2)
    # Maximum allowed spending in the period

    currency = models.CharField(max_length=10, default='NGN')
    # Currency of the budget (optional for multi-currency support)

    start_date = models.DateField()
    # Start of the budget period

    end_date = models.DateField()
    # End of the budget period

    is_active = models.BooleanField(default=True)
    # Whether this budget is currently active

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Timestamps for auditing and AI tracking

    class Meta:
        unique_together = ('user', 'category', 'start_date', 'end_date')
        # Prevent duplicate budgets for the same user, category, and period

    def __str__(self):
        return f"{self.user.username} - {self.category.name} Budget ({self.start_date} to {self.end_date})"