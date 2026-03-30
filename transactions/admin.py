from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'amount', 'currency', 'date', 'status')
    list_filter = ('type', 'status', 'currency')
    search_fields = ('user__username', 'description', 'category__name')
    ordering = ('-date',)
