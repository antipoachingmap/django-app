

from django.conf.urls import url
from antipoaching import views

# app_name = 'events'
# urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^$', views.events, name='index'),
    # url(r'^(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie_detail'),
    # url('reviews', views.reviews, name='reviews_index'),


urlpatterns = [
	url(r'^media/$', views.media_list),
	url(r'^media/(?P<pk>[0-9]+)/$', views.media_detail),
]