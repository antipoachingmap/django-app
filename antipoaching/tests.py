from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
setup_test_environment()


from .models import Event

class EventTests(TestCase):

	def test_403_at_root(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 403)

	def test_404_from_bad_url(self):
		client = Client()
		response = client.get('/asteroids')
		self.assertEqual(response.status_code, 404)
