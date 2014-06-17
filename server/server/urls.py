from django.conf.urls import patterns, include, url
from django.contrib import admin

from drops import urls as drops_urls
from trust import urls as trust_urls
from drops import api

import inspect
from tastypie.api import Api
from tastypie.resources import ModelResource


admin.autodiscover()

# create all of the api resources. use reflection instead of hard coding
# all of those guys in here.
v1_api = Api(api_name='v1')
for name, member in inspect.getmembers(api):
    if inspect.isclass(member) and\
       ModelResource in inspect.getmro(member) and\
       member is not ModelResource:
           v1_api.register(member())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(drops_urls)),
    url(r'^trust/', include(trust_urls)),
)
