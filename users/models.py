import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)

class Modules(models.TextChoices):
    FIRST_MODULE = 'Primeiro módulo'
    SECOND_MODULE = 'Segundo módulo'
    THIRD_MODULE = 'Terceiro módulo'
    FOURTH_MODULE = 'Quarto módulo'
    DEFAULT = 'Não especificado'

class User(AbstractUser):
    username = None

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=256, unique=True, verbose_name='Email Address')
    password = models.CharField(max_length=256)
    
    name = models.CharField(max_length=256, verbose_name='User\'s full name')
    course_module = models.CharField(choices=Modules.choices, default=Modules.DEFAULT, max_length=20)
    bio = models.TextField(max_length=512, default='A cool bio',null=False, verbose_name='Information about user')
    contact = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date of creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last date the field got update')

    avatar_url = models.CharField(max_length=256, null=True)

    REQUIRED_FIELDS = ['name', 'course_module', 'bio', 'contact']
    USERNAME_FIELD = 'email'

    objects = UserManager()
