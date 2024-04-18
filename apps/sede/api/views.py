from rest_framework.viewsets import ModelViewSet
from apps.sede.models import Sede
from apps.sede.api.serializers import SedeSerializer

class SedeViewSet(ModelViewSet):
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()