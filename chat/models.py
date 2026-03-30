from django.db import models

# Create your models here.
from users.models import CustomUser

class ChatMessage(models.Model):
    """
    Stores chat messages between user and AI assistant.
    Supports session tracking, message metadata, and AI recommendation links.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # The user sending the message

    message = models.TextField()
    # Message text from the user

    response = models.TextField(blank=True, null=True)
    # AI-generated response (optional if not yet generated)

    session_id = models.CharField(max_length=100, blank=True, null=True)
    # Group messages in sessions for chat continuity

    message_type = models.CharField(
        max_length=20,
        choices=(('text', 'Text'), ('command', 'Command'), ('recommendation', 'Recommendation')),
        default='text'
    )
    # Allows AI to categorize messages

    is_read = models.BooleanField(default=False)
    # Tracks whether the user has read the AI response

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Better than a single timestamp; allows updates if needed

    related_recommendation_id = models.IntegerField(blank=True, null=True)
    # Optional link to Recommendation model (for AI advice tracking)

    def __str__(self):
        return f"ChatMessage {self.id} - {self.user.username} ({self.created_at})"