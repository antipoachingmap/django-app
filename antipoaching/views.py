from django.shortcuts import render


from rest_framework import viewsets
from antipoaching.serializers import EventSerializer
from .models import Event

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        # 'snippets': reverse('snippet-list', request=request, format=format)
    })


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from antipoaching.models import Media
from antipoaching.serializers import MediaSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def media_list(request):
    """
    List all code media, or create a new media.
    """
    if request.method == 'GET':
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MediaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def media_detail(request, pk):
    """
    Retrieve, update or delete a code media.
    """
    try:
        media = Media.objects.get(pk=pk)
    except Media.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MediaSerializer(media)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MediaSerializer(media, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        media.delete()
        return HttpResponse(status=204)
# >>>>>>> media
from django.contrib.auth.models import User
from antipoaching.serializers import UserSerializer
from rest_framework import generics

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer



