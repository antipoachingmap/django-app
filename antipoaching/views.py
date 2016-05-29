from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from antipoaching.serializers import EventSerializer
from .models import Event

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer