from django.shortcuts import render
from .forms import PaymentForm
from django.http import HttpResponseRedirect
from django.views import View
from user.models import User
from django.contrib import messages
from decimal import Decimal

class PaymentView(View):

	form = PaymentForm()
	template = 'main.html'

	def get(self, request, *args, **kwargs):
		form = self.form
		return render(request, 'main.html', {'form': form})

	def post(self, request, *args, **kwargs):
		form = PaymentForm(request.POST)
		if form.is_valid():
			from_user = form.cleaned_data['from_user']
			to_users = form.cleaned_data['to_users']
			value = form.cleaned_data['value']
			if self.check_sum(value, from_user):
				self.process_payment(from_user, to_users.split(" "), value)
			return HttpResponseRedirect('/')

		return render(request, 'main.html', {'form': form})

	def check_sum(self, value, user):
		if user.funds < Decimal(value):
			return False
		return True

	def process_payment(self, from_user, to_users, value):
		value = Decimal(value)
		f_u = from_user
		t_u = to_users
		f_u.funds -= value
		f_u.save()
		single_sum = value / len(t_u)
		for target in t_u:
			u = User.objects.get(inn=target)
			u.funds += single_sum
			u.save()