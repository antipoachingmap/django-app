from django.test import TestCase

from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json

from .models import Media

client = APIClient()

def create_media_object():
	return Media.objects.create(
		description='A party parrot',
		format='png',
		timestamp=1463322187,
		filename='party_parrot',
		filesize=500123
	)

def create_user():
	return User.objects.create(
			username='Richard Nixon',
			password='I am not a crook'
		)

# Create your tests here.
class MediaAPITests(TestCase):
	def test_create_media_object(self):

		response = client.post('/v1/media/', {
			'description': 'A party parrot',
			'format': 'png',
			'timestamp': 1463322187,
			'filename': 'party_parrot',
			'filesize': 500123
		})

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 201)
		self.assertEqual(data['description'], 'A party parrot')
		self.assertEqual(data['format'], 'png')
		self.assertEqual(data['timestamp'], 1463322187)
		self.assertEqual(data['filename'], 'party_parrot')
		self.assertEqual(data['filesize'], 500123)

	def test_list_media_objects(self):

		create_media_object()

		response = client.get('/v1/media/')

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(data), 1)

	def test_detail_media_object(self):

		record = create_media_object()

		response = client.get('/v1/media/' + str(record.id) + '/')

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['description'], 'A party parrot')
		self.assertEqual(data['format'], 'png')
		self.assertEqual(data['timestamp'], 1463322187)
		self.assertEqual(data['filename'], 'party_parrot')
		self.assertEqual(data['filesize'], 500123)


	def test_update_media_object(self):

		record = create_media_object()

		response = client.put('/v1/media/' + str(record.id) + '/', {
			'description': 'A party pangolin',
			'format': 'png',
			'timestamp': 1463322187,
			'filename': 'party_pangolin',
			'filesize': 500666
		})

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['description'], 'A party pangolin')
		self.assertEqual(data['format'], 'png')
		self.assertEqual(data['timestamp'], 1463322187)
		self.assertEqual(data['filename'], 'party_pangolin')
		self.assertEqual(data['filesize'], 500666)

	def test_delete_media_object(self):

		record = create_media_object()

		response = client.delete('/v1/media/' + str(record.id) + '/')
		self.assertEqual(response.status_code, 204)

class EventTests(TestCase):

	def test_200_at_root(self):
		response = client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_404_from_bad_url(self):
		response = client.get('/asteroids/')
		self.assertEqual(response.status_code, 404)

	def test_200_for_events(self):
		response = client.get('/v1/events/')
		self.assertEqual(response.status_code, 200)

	def test_getting_list_of_events(self):

		response = client.get(API + 'v1/events/')
		self.assertEqual(response.status_code, 200)
		self.assertTrue('count' in response.data)
		self.assertTrue('next' in response.data)
		self.assertTrue('previous' in response.data)
		self.assertTrue('results' in response.data)


class AuthTests(TestCase):

	def test_credentials(self):
		create_user()
		response = client.post('/v1/auth', {'username': 'Richard Nixon', 'password': 'I am not a crook'})
		print response

