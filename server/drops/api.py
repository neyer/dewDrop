from tastypie.resources import ModelResource


from drops.models import Identity
from drops.models import Network
from drops.models import Statement


class NetworkResource(ModelResource):
    class Meta:
        queryset = Network.objects.all()

class IdentityResource(ModelResource):
    class Meta:
        queryset = Identity.objects.all()


class StatementResource(ModelResource):
    class Meta:
        queryset = Statement.objects.all()
