from django.db import models
from django.contrib.auth.models import AbstractUser
from .validator import validate_inn
from payments.validator import check_decimal
# Create your models here.


class User(AbstractUser):
	inn = models.CharField(max_length=15, validators=[validate_inn])
	funds = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, validators=[check_decimal])
