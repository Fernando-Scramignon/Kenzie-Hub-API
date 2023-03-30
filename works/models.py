from django.db import models
from users.models import User
from uuid import uuid4

class Work(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=256, verbose_name='work name')
    deploy_url = models.CharField(max_length=512, verbose_name='application address')
    description = models.TextField(max_length=512, verbose_name='work description')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date of creation')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date of last modification')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='works')