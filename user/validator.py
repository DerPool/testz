from django.core.exceptions import ValidationError


def validate_inn(value):
	if not (all([a.isdigit() for a in value])):
		raise ValidationError("Некорректный ИНН",)