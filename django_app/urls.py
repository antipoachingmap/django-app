from django.conf.urls import url, include
from django.contrib import admin

from antipoaching import views as antipoachingviews
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'v1/events', antipoachingviews.EventViewSet)
router.register(r'v1/media', antipoachingviews.MediaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]


