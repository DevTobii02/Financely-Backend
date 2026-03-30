from django.db import models
from users.models import CustomUser
from transactions.models import Transaction

# Create your models here.

class MLModelLog(models.Model):
    """
    Tracks AI/ML models, their training, usage, and metadata for each user.
    """

    MODEL_TYPE_CHOICES = (
        ('classifier', 'Classifier'),
        ('regressor', 'Regressor'),
        ('recommendation', 'Recommendation'),
        ('forecasting', 'Forecasting'),
        ('other', 'Other'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Owner of the ML model

    model_name = models.CharField(max_length=100)
    # Identifier for the model

    model_type = models.CharField(max_length=20, choices=MODEL_TYPE_CHOICES, default='other')
    # Categorize the type of AI/ML model

    related_transaction = models.ForeignKey(
        Transaction,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    # Optional: link to a transaction dataset that trained or influenced the model

    trained_on = models.DateTimeField(auto_now_add=True)
    # When the model was trained

    accuracy = models.FloatField(null=True, blank=True)
    # Accuracy or performance metric (optional)

    version = models.PositiveIntegerField(default=1)
    # Versioning of the model for tracking improvements

    last_used = models.DateTimeField(auto_now=True)
    # Last time the model was used

    notes = models.TextField(blank=True, null=True)
    # Optional notes: hyperparameters, training dataset details, purpose

    is_active = models.BooleanField(default=True)
    # Whether the model is currently active for predictions

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Timestamps for consistent tracking

    class Meta:
        unique_together = ('user', 'model_name', 'version')
        # Prevent duplicate model name + version for same user

    def __str__(self):
        return f"{self.model_name} v{self.version} ({self.user.username})"