from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
	inn = models.CharField(max_length=15)
	funds = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
