from tastypie.resources import ModelResource


from drops.models import Address
from drops.models import Network
from drops.models import Statement


class NetworkResource(ModelResource):
    class Meta:
        queryset = Network.objects.all()

class AddressResource(ModelResource):
    class Meta:
        queryset = Address.objects.all()


class StatementResource(ModelResource):
    class Meta:
        queryset = Statement.objects.all()
