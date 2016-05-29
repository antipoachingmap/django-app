from .models import Event
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
	events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

	class Meta:
		model = Userfields = ('id', 'username', 'events')


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
