from django.db import models
from users.models import CustomUser
from transactions.models import Transaction
from accounts.models import Account
from categories.models import Category
from budgets.models import Budget
from bills.models import Bill
from notifications.models import Notification

# Create your models here.

class RecurringTransaction(models.Model):
    """
    Represents transactions that occur on a recurring schedule, 
    such as salaries, subscriptions, or bills.
    """

    FREQUENCY_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('biweekly', 'Bi-Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    )

    TRANSACTION_TYPE = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Owner of the recurring transaction

    transaction = models.ForeignKey(
        'transactions.Transaction', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        related_name='recurring_transactions'
    )
    # Optional reference to the original transaction for AI/analytics

    name = models.CharField(max_length=100)
    # Description or name of the recurring transaction (e.g., "Netflix Subscription")

    account = models.ForeignKey(
        Account, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    # Account from which this recurring transaction occurs

    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    # Category for tracking purposes (Income, Expense, Salary, Subscription, etc.)

    bill = models.ForeignKey(
        Bill, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    # Optional: link to a bill for automatic reminders and AI insights

    budget = models.ForeignKey(
        Budget,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    # Optional: link to a budget for spending tracking

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    # Amount of each recurring transaction

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    # Income or Expense

    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='monthly')
    # How often this transaction recurs

    start_date = models.DateField()
    # Start date for the recurring transaction

    end_date = models.DateField(blank=True, null=True)
    # Optional end date (None = indefinite)

    next_due_date = models.DateField()
    # The next date this transaction is due

    is_active = models.BooleanField(default=True)
    # Whether the recurring transaction is currently active

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Timestamps for tracking and analytics

    notification = models.ForeignKey(
        Notification,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    # Optional notification associated with this recurring transaction

    notes = models.TextField(blank=True, null=True)
    # Optional notes or details

    class Meta:
        unique_together = ('user', 'name', 'account', 'start_date')
        # Prevent duplicate recurring transactions for the same user/account/start date

    def __str__(self):
        return f"{self.name} ({self.transaction_type}) - {self.user.username}"