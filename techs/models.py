from django.db import models
from uuid import uuid4

class StatusChoices(models.TextChoices):
    BEGINNER = 'Iniciante'
    INTERMEDIATE = 'Intermediário'
    ADVANCED = 'Avançado'


class Tech(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=256)
    status = models.CharField(max_length=256, choices=StatusChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date of creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date of last modification')
