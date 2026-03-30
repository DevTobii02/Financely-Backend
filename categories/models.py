from django.db import models
from users.models import CustomUser

# Create your models here.

class Category(models.Model):
    """
    Transaction category (Income or Expense) per user.
    Includes metadata for AI insights, analytics, and management.
    """

    CATEGORY_TYPE = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Owner of the category

    name = models.CharField(max_length=100)
    # Name of category, e.g., 'Salary', 'Groceries'

    type = models.CharField(max_length=10, choices=CATEGORY_TYPE)
    # Income or Expense

    description = models.TextField(blank=True, null=True)
    # Optional description for AI/analytics insights

    is_active = models.BooleanField(default=True)
    # Can be used to archive categories without deleting

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Track creation and modification for analytics and AI

    class Meta:
        unique_together = ('user', 'name', 'type')
        # Prevent duplicate category names of same type per user

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.user.username}"