from django.core.exceptions import ValidationError
from decimal import Decimal


def validate_inn(value):
    if not (all([a.isdigit() for a in value])):
        raise ValidationError("Некорректный ИНН",)


def check_decimal(value):
    try:
        a = Decimal(value)
        if a < 0:
            raise ValidationError("Incorrect value",)
    except:
        raise ValidationError("Incorrect value",)
