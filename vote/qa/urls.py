from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.splash, name='splash'),
    re_path(r'^questions$', views.index, name='questions'),
    # re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
