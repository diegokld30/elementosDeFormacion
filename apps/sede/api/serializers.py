from rest_framework import serializers
from apps.sede.models import Sede
from apps.municipios.api.serializers import MunicipioSerializer

class SedeSerializer(serializers.ModelSerializer):
    centro_sede = MunicipioSerializer()
    class Meta:
        model = Sede
        fields = ['nombre_sede', 'centro_sede', 'direccion_sede', 'date_created', 'date_modified']