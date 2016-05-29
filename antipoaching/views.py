from rest_framework import viewsets
from antipoaching.serializers import EventSerializer, MediaSerializer
from .models import Event, Media

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
