from django import forms
from user.models import User 
from .validator import check_to_users, check_decimal


class PaymentForm(forms.Form):
	from_user = forms.ModelChoiceField(queryset=User.objects.all())
	to_users = forms.CharField(validators=[check_to_users], widget=forms.Textarea, initial="Введите ИНН через пробел")
	value = forms.CharField(validators=[check_decimal], initial="0.01")


