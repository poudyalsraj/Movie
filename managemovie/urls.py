from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView
app_name='managemovie'

urlpatterns=[

	url(r'^$', views.MovieGenreListView.as_view(), name='home'),
	url(r'^(?P<pk>\d+)/$', views.MovieGenreDetailView.as_view(), name='moviegenre-detail'),
	url(r'^add/genre$', views.MovieGenreCreateView.as_view(), name='moviegenre-add'),
	url(r'^(\d+)/delete//$', views.MovieGenreDeleteView.as_view(), name='moviegenre-delete'),

	url(r'^movie$', views.MovieListView.as_view(), name='movie-list'),

	url(r'^add/movie$', views.MovieCreateView.as_view(), name='movie-add'),

	url(r'^(?P<gid>\d+)/update/(?P<pk>\d+)/$', views.MovieUpdateView.as_view(), name='movie-update'),

	url(r'^(\d+)/delete/(?P<pk>\d+)/$', views.MovieDeleteView.as_view(), name='movie-delete'),
	
	url(r'^(\d+)/detail/(?P<pk>\d+)/$', views.MovieDetailView.as_view(), name='movie-detail'),

	

]