from django.core.exceptions import ValidationError
from user.models import User
from decimal import Decimal


def check_to_users(value):
	targets = value.split(" ")
	for target in targets: 
		try:
			User.objects.get(inn=target)
		except User.DoesNotExist:
			raise ValidationError(("User with inn: ", target, " does not exists"),)


def check_decimal(value):
	try:
		a = Decimal(value)
		if a < 0:
			raise ValidationError("Incorrect value",)
	except:
		raise ValidationError("Incorrect value",)