
from drops.models import Address
from drops.models import Network
from drops.models import Statement

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ALL
from tastypie.resources import ALL_WITH_RELATIONS
from tastypie.resources import ModelResource


class NetworkResource(ModelResource):
    class Meta:
        queryset = Network.objects.all()
        filtering = {
                'id' : ALL,
                'name' : ALL,
        }

class AddressResource(ModelResource):
    network = fields.ForeignKey(NetworkResource, 'network',
                                full=True)
    class Meta:
        queryset = Address.objects.all()
        filtering  = {
                'id': ALL_WITH_RELATIONS,
                'network': ALL_WITH_RELATIONS,
                'name': ALL_WITH_RELATIONS,
        }

class StatementResource(ModelResource):

    author = fields.ToOneField(AddressResource,
                               'author',
                                full=True)
    subject = fields.ToOneField(AddressResource,
                                'subject',
                                full=True)
    class Meta:
        queryset = Statement.objects.all()
        authorization = Authorization()

        filtering = {
                'author' : ALL_WITH_RELATIONS,
                'subject' : ALL_WITH_RELATIONS,
                'content' : ALL_WITH_RELATIONS,
                'timestamp' : ALL_WITH_RELATIONS,
        }

