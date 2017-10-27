
from django.conf.urls import url
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^make_plan_page/$', views.make_plan_page),
    url(r'^create$', views.create),
    url(r'^trip_view$', views.trip_view),
    url(r'^dashboard/trip/remove/(?P<id>\d+)$', views.removeOwner),
    url(r'^dashboard/trip/add/(?P<id>\d+)$', views.addOwner),
    url(r'^trip_view/(?P<id>\d+)$', views.trip_view),
]
