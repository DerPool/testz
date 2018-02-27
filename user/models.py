from django.db import models
from django.contrib.auth.models import AbstractUser
from .validator import validate_inn
from django.contrib.auth.base_user import BaseUserManager
from .validator import check_decimal
# Create your models here.

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Username must be set")
        if extra_fields['inn']:
            validate_inn(extra_fields['inn'])
        if extra_fields['funds']:
            check_decimal(extra_fields['funds'])
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

            return self._create_user(username, password, **extra_fields)


class User(AbstractUser):
    inn = models.CharField(max_length=15, validators=[validate_inn])
    funds = models.DecimalField(validators=[check_decimal],
                                max_digits=8, decimal_places=2, default=0.00)
    objects = CustomUserManager()


