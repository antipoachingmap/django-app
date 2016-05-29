from django.test import TestCase

# Create your tests here.
class MediaAPITests(TestCase):
	def test_creating_media_object(self):
		response = self.client.post('/media', {
			description: 'A party parrot',
			format: 'png',
			timestamp: 1463322187,
			filename: 'part_parrot',
			filesize: 500123
		})

		self.assertEqual(response.status_code, 200)