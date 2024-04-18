from rest_framework.viewsets import ModelViewSet
from apps.ficha.models import Ficha
from apps.ficha.api.serializers import FichaSerializer
class FichaViewSet(ModelViewSet):
    serializer_class = FichaSerializer
    queryset = Ficha.objects.all()