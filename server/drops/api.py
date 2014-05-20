from tastypie.resources import ModelResource


from drops.models import Identity
from drops.models import Network
from drops.models import Statement


class NetworkResource(ModelResource):
    class Meta:
        queryset = Network.objects.all()
