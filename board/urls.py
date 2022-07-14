from django.urls import re_path
from . import views

app_name = 'board'

urlpatterns = [
    re_path(r'^$', views.top_screen, name="top-screen"),
    re_path(r'^create/$', views.create, name="create"),
    re_path(r'^detail/(?P<art>\d{1,10})/$', views.detail, name="detail"),
    re_path(r'^delete/(?P<art>\d{1,10})/$', views.delete, name="delete"),
    re_path(r'^edit/(?P<art>\d{1,10})/$', views.edit, name="edit"),
]