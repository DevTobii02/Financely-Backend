from django.db import models
from users.models import CustomUser

class Account(models.Model):
    """
    Represents a financial account (bank, cash, wallet).
    """

    ACCOUNT_TYPE = (
        ('bank', 'Bank'),
        ('cash', 'Cash'),
        ('wallet', 'Wallet'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Links account to a user

    name = models.CharField(max_length=100)
    # Example: "GTBank Savings"

    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Current account balance

    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    # Restricted to predefined values

    currency = models.CharField(max_length=10, default='NGN')
    # Currency of the account (e.g., NGN, USD, GBP)

    created_at = models.DateTimeField(auto_now_add=True)
    # When account was created

    def __str__(self):
        return f"{self.name} ({self.account_type}) - {self.currency}"