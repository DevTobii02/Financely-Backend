from django.db import models

# Create your models here.
from users.models import CustomUser
from categories.models import Category
from accounts.models import Account
from budgets.models import Budget
from goals.models import Goal
from bills.models import Bill

class Transaction(models.Model):
    """
    Represents a financial transaction by a user.
    Supports AI insights, budgets, goals, recurring transactions, and notifications.
    """

    TRANSACTION_TYPE = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default='NGN')
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    recurring = models.BooleanField(default=False)
    # Indicates if this transaction is part of a recurring series
    recurring_transaction = models.ForeignKey(
        'recurring_transactions.RecurringTransaction', 
        on_delete=models.SET_NULL, 
        null=True, blank=True,
        related_name='transactions'
    )

    budget = models.ForeignKey(Budget, on_delete=models.SET_NULL, blank=True, null=True)
    goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, blank=True, null=True)
    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, blank=True, null=True)
    notification = models.ForeignKey('notifications.Notification', on_delete=models.SET_NULL, blank=True, null=True, related_name='transactions')
    # Optional links for AI, budgets, goals, bills, and notifications

    status = models.CharField(max_length=20, default='completed')
    # Could be 'pending', 'completed', 'failed', etc.

    class Meta:
        ordering = ['-date']
        # Most recent transactions appear first

    def __str__(self):
        return f"{self.user.username} - {self.type}: {self.amount} {self.currency} ({self.category.name if self.category else 'Uncategorized'})"