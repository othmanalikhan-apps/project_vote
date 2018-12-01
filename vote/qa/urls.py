from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.splash, name='splash'),
    re_path(r'^questions$', views.questions, name='questions'),
    # re_path(r'^about$', views.about, name='about'),
    re_path(r'^new_question$', views.new_question, name='new_question'),
    # re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
