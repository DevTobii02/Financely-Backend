from django.db import models

# Create your models here.
from users.models import CustomUser

class Recommendation(models.Model):
    """
    Stores AI-generated financial recommendations for users.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # The user receiving the recommendation

    transaction = models.ForeignKey(
        'transactions.Transaction',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # Optional link to a related transaction
    # SET_NULL prevents losing recommendation if transaction is deleted

    message = models.TextField()
    # The AI-generated recommendation text

    created_at = models.DateTimeField(auto_now_add=True)
    # When the recommendation was created

    implemented = models.BooleanField(default=False)
    # Whether the user followed the recommendation

    def __str__(self):
        return f"Recommendation for {self.user.username}"