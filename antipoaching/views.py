from django.shortcuts import render

from rest_framework import viewsets
from antipoaching.serializers import MediaSerializer
from .models import Media

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer