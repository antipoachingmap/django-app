from .models import Event
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        # fields = ('description')
        fields = ('__all__')


from antipoaching.models import Media

class MediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		fields = ('id', 'description', 'format', 'timestamp', 'filename', 'filesize')
