from rest_framework.viewsets import ModelViewSet
from apps.elemento_material.api.serializers import ElementoMaterialSerializer
from apps.elemento_material.models import ElementoMaterial

class ElementoMaterialViewSet(ModelViewSet):
    serializer_class = ElementoMaterialSerializer
    queryset = ElementoMaterial.objects.all()