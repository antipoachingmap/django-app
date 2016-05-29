from django.test import TestCase

from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json

from .models import Media, Event

client = APIClient()

def create_media_object():
	return Media.objects.create(
		description='A party parrot',
		format='png',
		timestamp=1463322187,
		filename='party_parrot',
		filesize=500123
	)

# Create your tests here.
class MediaTests(TestCase):

	def setUp(self):
		user = User.objects.create_user('admin', 'admin@test.com', 'password123')
		user.save()
		client.force_authenticate(user=user)

	def test_create_media(self):

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


	def test_list_media(self):

		create_media_object()

		response = client.get('/v1/media/')

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(data), 1)


	def test_detail_media(self):

		record = create_media_object()

		response = client.get('/v1/media/' + str(record.id) + '/')

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['description'], 'A party parrot')
		self.assertEqual(data['format'], 'png')
		self.assertEqual(data['timestamp'], 1463322187)
		self.assertEqual(data['filename'], 'party_parrot')
		self.assertEqual(data['filesize'], 500123)


	def test_update_media(self):

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


	def test_delete_media(self):

		record = create_media_object()

		response = client.delete('/v1/media/' + str(record.id) + '/')
		self.assertEqual(response.status_code, 204)

def create_event_object():
	return Event.objects.create(
		description='Asteroid strike',
		severity='c',
		timestamp=1463322187,
		lat=42.42,
		long=101.45,
		extra='{"someJson":"Some more json"}'
	)

class EventTests(TestCase):

	def setUp(self):
		user = User.objects.create_user('admin', 'admin@test.com', 'password123')
		user.save()
		client.force_authenticate(user=user)

	def test_create_event(self):

		response = client.post('/v1/events/', {
			'description': 'Asteroid strike',
			'severity': 'c',
			'timestamp': 1463322187,
			'lat': 42.42,
			'long': 101.45,
			'extra': '{"someJson":"Some more json"}'
		})

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 201)
		self.assertEqual(data['description'], 'Asteroid strike')
		self.assertEqual(data['severity'], 'c')
		self.assertEqual(data['timestamp'], 1463322187)
		self.assertEqual(data['lat'], 42.42)
		self.assertEqual(data['long'], 101.45)
		self.assertEqual(data['extra'], '{"someJson":"Some more json"}')


	def test_list_events(self):

		create_event_object()

		response = client.get('/v1/events/')

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(data), 1)	


	def test_detail_event(self):

		record = create_event_object()

		response = client.get('/v1/events/' + str(record.id) + '/')

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['description'], 'Asteroid strike')
		self.assertEqual(data['severity'], 'c')
		self.assertEqual(data['timestamp'], 1463322187)
		self.assertEqual(data['lat'], 42.42)
		self.assertEqual(data['long'], 101.45)
		self.assertEqual(data['extra'], '{"someJson":"Some more json"}')


	def test_update_object(self):

		record = create_event_object()

		response = client.put('/v1/events/' + str(record.id) + '/', {
			'description': 'Comet attack',
			'severity': 'c',
			'timestamp': 1463322187,
			'lat': 42.42,
			'long': 101.45,
			'extra': '{"someJson":"Some more json"}'
		})

		data = json.loads(response.content)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['description'], 'Comet attack')
		self.assertEqual(data['severity'], 'c')
		self.assertEqual(data['timestamp'], 1463322187)
		self.assertEqual(data['lat'], 42.42)
		self.assertEqual(data['long'], 101.45)
		self.assertEqual(data['extra'], '{"someJson":"Some more json"}')


	def test_delete_event(self):

		record = create_event_object()

		response = client.delete('/v1/events/' + str(record.id) + '/')
		self.assertEqual(response.status_code, 204)


class AuthTests(TestCase):

	def setUp(self):
		self.admin = User.objects.create_user('admin', 'admin@test.com', 'password123')
		self.admin.save()

	def test_credentials(self):
		response = client.post('/v1/auth/', {'username': 'admin', 'password': 'password123'})
		self.assertEqual(response.status_code, 200)