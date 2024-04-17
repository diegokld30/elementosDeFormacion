from rest_framework import serializers
from apps.sitio.models import Sitio
from apps.users.api.serializers import UserSerializer
from apps.tipo_sitio.api.serializers import Tipo_sitioSerializer

class SitioSerializer(serializers.ModelSerializer):
    persona_encargada = UserSerializer()
    tipo_sitio = Tipo_sitioSerializer()
    class Meta:
        model = Sitio
        fields = ['persona_encargada','nombre_sitio','tipo_sitio', 'ubicacion', 'FichaTecnica', 'date_created', 'date_modified']

