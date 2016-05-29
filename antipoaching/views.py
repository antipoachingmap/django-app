from rest_framework import viewsets
from antipoaching.serializers import EventSerializer, MediaSerializer
from .models import Event, Media
from rest_framework import permissions

class EventViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MediaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
