from rest_framework import serializers
from antipoaching.models import Media

class MediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		fields = ('id', 'description', 'format', 'timestamp', 'filename', 'filesize')