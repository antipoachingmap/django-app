from django.conf.urls import url, include
from django.contrib import admin

from antipoaching import views as antipoachingviews
from rest_framework import routers
from rest_framework.authtoken import views as authviews

router = routers.DefaultRouter()

router.register(r'v1/events', antipoachingviews.EventViewSet)
router.register(r'v1/media', antipoachingviews.MediaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/auth/', authviews.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
]