from .models import Event, Media
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('__all__')

class MediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		fields = ('__all__')
