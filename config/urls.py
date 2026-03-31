"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('ai_assistant.urls')),
    path('api/', include('analytics.urls')),
    path('api/', include('app_settings.urls')),
    path('api/', include('bills.urls')),
    path('api/', include('budgets.urls')),
    path('api/', include('categories.urls')),
    path('api/', include('chat.urls')),
    path('api/', include('currency.urls')),
    path('api/', include('data.urls')),
    path('api/', include('goals.urls')),
    path('api/', include('integrations.urls')),
    path('api/', include('ml_engine.urls')),
    path('api/', include('notifications.urls')),
    path('api/', include('recurring_transactions.urls')),
    path('api/', include('security.urls')),
    path('api/', include('transactions.urls')),
    path('api/', include('users.urls')),
]
