from django.conf.urls import patterns, include, url
from django.contrib import admin

from drops import urls as drops_urls
from drops import api

# implement all the admin urls
network_resource = api.NetworkResource()

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(network_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(drops_urls)),
)
