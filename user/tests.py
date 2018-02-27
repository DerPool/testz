from django.test import TestCase
from django.test import Client
from .models import User
# Create your tests here.
from django.core.exceptions import ValidationError
class SetupUser(TestCase):
	def setUp(self):
		pass


class UserCreation_testcase(SetupUser):
	def testuser_creation_valid(self):

		self.user = User.objects.create_user(username="test2", password="qwerty123", inn="12464272", funds="12.34")
		self.assertEqual(User.objects.get(username='test2'), self.user)

	def testuser_creation_invalid_inn(self):
		try:
			User.objects.create_user(username="test3", password="qwerty123", inn="aeet12354 qwe", funds="12.34")
			self.fail("Test failed")
		except ValidationError:
			self.assertTrue(True)
		
	def testuser_creation_invalid_funds(self):
		try:
			User.objects.create_user(username="test4", password="qwerty123", inn="123345", funds="-10.11")
			self.fail("Test failed")
		except ValidationError:
			self.assertTrue(True)