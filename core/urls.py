# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate_webhook', views.generate_webhook, name='generate_webhook'),
    path('webhook/<str:token>', views.webhook, name='webhook'),
]
