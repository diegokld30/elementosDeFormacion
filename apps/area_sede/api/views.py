from rest_framework.viewsets import ModelViewSet
from apps.area_sede.models import AreaSede
from apps.area_sede.api.serializers import AreaSedeSerializer

class AreaSedeViewSet(ModelViewSet):
    serializer_class = AreaSedeSerializer
    queryset = AreaSede.objects.all()