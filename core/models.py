# core/models.py
from django.db import models

class WebhookToken(models.Model):
    token = models.CharField(max_length=16, unique=True)
    data = models.JSONField()
