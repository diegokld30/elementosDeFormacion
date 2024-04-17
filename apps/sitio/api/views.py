from rest_framework.viewsets import ModelViewSet
from apps.sitio.api.serializers import SitioSerializer
from apps.sitio.models import Sitio


class SitioViewSet(ModelViewSet):
    serializer_class = SitioSerializer
    queryset = Sitio.objects.all()