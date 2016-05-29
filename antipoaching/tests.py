from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
setup_test_environment()
from .models import Event

API = 'http://localhost:8000/'

class EventTests(TestCase):

	def test_200_at_root(self):
		client = Client()
		response = client.get(API)
		self.assertEqual(response.status_code, 200)

	def test_404_from_bad_url(self):
		client = Client()
		response = client.get(API + 'asteroids/')
		self.assertEqual(response.status_code, 404)

	def test_getting_list_of_events(self):
		client = Client()
		response = client.get(API + 'v1/events/')
		self.assertEqual(response.status_code, 200)
		self.assertTrue('count' in response.data)
		self.assertTrue('next' in response.data)
		self.assertTrue('previous' in response.data)
		self.assertTrue('results' in response.data)

