from rest_framework.viewsets import ModelViewSet
from apps.programa.models import Programa
from apps.programa.api.serializers import ProgramaSerializer

class ProgramaViewSet(ModelViewSet):
    serializer_class = ProgramaSerializer
    queryset = Programa.objects.all()