

from django.conf.urls import url
from antipoaching import views


urlpatterns = [
	url(r'^media/$', views.media_list),
	url(r'^media/(?P<pk>[0-9]+)/$', views.media_detail),
]
