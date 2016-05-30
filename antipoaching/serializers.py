from .models import Event, Media
from rest_framework_mongoengine import serializers


class EventSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Event
        depth = 2

class MediaSerializer(serializers.DocumentSerializer):
	class Meta:
		model = Media
