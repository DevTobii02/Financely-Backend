from django.db import models

# Create your models here.
from users.models import CustomUser
from categories.models import Category


class Bill(models.Model):
    """
    Represents a bill (e.g., rent, electricity, Netflix subscription).
    """

    BILL_FREQUENCY = (
        ('one_time', 'One Time'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )

    BILL_STATUS = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Owner of the bill

    name = models.CharField(max_length=255)
    # Example: "Electricity Bill"

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    # Expected bill amount

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # Optional categorization

    due_date = models.DateField()
    # When payment is due

    frequency = models.CharField(
        max_length=20,
        choices=BILL_FREQUENCY,
        default='monthly'
    )
    # Recurrence type

    status = models.CharField(
        max_length=20,
        choices=BILL_STATUS,
        default='pending'
    )
    # Current state of the bill

    is_active = models.BooleanField(default=True)
    # Whether bill is still relevant

    auto_pay = models.BooleanField(default=False)
    # Future: integrate with payment automation

    reminder_days_before = models.PositiveIntegerField(default=3)
    # Notify user before due date

    last_paid_date = models.DateField(null=True, blank=True)
    # Tracks last payment

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class BillPayment(models.Model):
    """
    Tracks payments made toward bills.
    Links to transactions for financial records.
    """

    PAYMENT_METHODS = (
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('card', 'Card'),
        ('mobile_money', 'Mobile Money'),
    )

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    # Amount actually paid

    payment_date = models.DateField()
    # When payment occurred

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    reference = models.CharField(max_length=255, null=True, blank=True)
    # Transaction reference (optional)

    notes = models.TextField(blank=True, null=True)
    # Optional user notes

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bill.name} - {self.amount_paid}"