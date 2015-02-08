from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls'), name='api'),
    url(r'^(?P<pin>[A-Za-z0-9]{1,15})/$', 'api.views.register', name='register'),
)
