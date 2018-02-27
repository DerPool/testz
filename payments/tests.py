from django.test import TestCase
from django.test import Client
from .forms import PaymentForm
# Create your tests here.
from user.models import User




class SetupUser(TestCase):
	def setUp(self):
		self.user = User.objects.create(email="asda@gmail.com", password="1234556", username="test", inn='123321', funds=120.01)
		self.user2 = User.objects.create(email="assda@gmail.com", password="1234556", username="test2", inn='1233222', funds=100.00)



class TestView(SetupUser):
	def testFormValidators_valid_data(self):

		self.form = PaymentForm(data={'from_user': self.user, 'to_users': '123321adas', 'value': '50.00'})
		self.assertEqual()

	def testFormValidators_invalid_data(self):
		self.form = PaymentForm(data={'from_user': self.user, 'to_users': '123322asdasd2', 'value': '50.00'})
		self.assertFalse(self.form.is_valid())
