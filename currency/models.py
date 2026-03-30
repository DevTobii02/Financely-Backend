from django.db import models

# Create your models here.

class Currency(models.Model):
    """
    Represents a currency, e.g., Nigerian Naira (NGN), US Dollar (USD), Euro (EUR).
    """
    code = models.CharField(max_length=10, unique=True)
    # Currency code (ISO 4217 standard), e.g., 'USD', 'NGN'

    name = models.CharField(max_length=50)
    # Full currency name, e.g., 'United States Dollar'

    symbol = models.CharField(max_length=10, blank=True, null=True)
    # Optional symbol, e.g., '$', '₦', '€'

    is_active = models.BooleanField(default=True)
    # Whether the currency is available for new transactions

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Timestamps for tracking creation and updates

    def __str__(self):
        return f"{self.code} - {self.name}"


class ExchangeRate(models.Model):
    """
    Stores exchange rates between currencies.
    Useful for multi-currency transactions and analytics.
    """
    from_currency = models.ForeignKey(
        Currency,
        related_name='exchange_from',
        on_delete=models.CASCADE
    )
    # Base currency

    to_currency = models.ForeignKey(
        Currency,
        related_name='exchange_to',
        on_delete=models.CASCADE
    )
    # Target currency

    rate = models.DecimalField(max_digits=20, decimal_places=6)
    # Exchange rate: multiply amount in from_currency by this to get to_currency

    date = models.DateField(auto_now_add=True)
    # Date when the exchange rate was recorded

    is_active = models.BooleanField(default=True)
    # Whether this rate is current

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('from_currency', 'to_currency', 'date')
        # Prevent duplicate rates for same currency pair on same date

    def __str__(self):
        return f"{self.from_currency.code} → {self.to_currency.code} = {self.rate}"