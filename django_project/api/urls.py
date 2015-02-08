from django.conf.urls import patterns, url


urlpatterns = patterns('',
    #url(r'^whoshome/', 'views.whoshome', name='whoshome'),
    url(r'^(?P<tag_uuid>\d{1,15})/$', 'api.views.process', name='process'),
)
