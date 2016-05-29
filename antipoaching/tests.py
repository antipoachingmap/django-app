from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
class MediaAPITests(TestCase):
	def test_creating_media_object(self):

		client = APIClient()

		response = client.post('/v1/media/', {
			'description': 'A party parrot',
			'format': 'png',
			'timestamp': '2016-05-29T16:40',
			'filename': 'part_parrot',
			'filesize': 500123
		})

		print response.content

		self.assertEqual(response.status_code, 201)