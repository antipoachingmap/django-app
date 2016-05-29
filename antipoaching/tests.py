from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
class MediaAPITests(TestCase):
	def test_creating_media_object(self):

		client = APIClient()

		response = client.post('/v1/media/', {
			'description': 'A party parrot',
			'format': 'png',
			'timestamp': 1463322187,
			'filename': 'part_parrot',
			'filesize': 500123
		})

		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.content, '{"id":1,"description":"A party parrot","format":"png","timestamp":1463322187,"filename":"part_parrot","filesize":500123}')

	def test_listing_media_objects(self):

		client = APIClient()

		response = client.get('/v1/media/')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, '[]')