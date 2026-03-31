# transactions/serializers.py
from rest_framework import serializers
from .models import Transaction  # import your model

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"  # or list specific fields: ['id', 'title', 'amount']