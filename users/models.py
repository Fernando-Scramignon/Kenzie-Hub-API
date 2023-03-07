import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class Modules(models.TextChoices):
    FIRST_MODULE = 'Primeiro módulo'
    SECOND_MODULE = 'Segundo módulo'
    THIRD_MODULE = 'Terceiro módulo'
    FOURTH_MODULE = 'Quarto módulo'
    DEFAULT = 'Não especificado'

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=256, unique=True, verbose_name='Email Address')
    password = models.CharField(max_length=256, null=False, blank=False)
    
    name = models.CharField(max_length=256, null=False, blank=False)
    course_module = models.CharField(choices=Modules.choices, default=Modules.DEFAULT, max_length=20, null=False, blank=False)
    bio = models.TextField(max_length=512, default='A cool bio',null=False, verbose_name='Information about user')

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date of creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last date the field got update')

    avatar_url = models.CharField(max_length=256, null=True)
