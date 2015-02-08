from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^(?P<tag_uuid>\d+)/$', views.process, name='process'),
    url(r'^whoshome/$', views.whoshome, name='whoshome'),
)
