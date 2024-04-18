from rest_framework import serializers
from apps.centro.models import Centro
from apps.municipios.api.serializers import MunicipioSerializer

class CentroSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer()
    class Meta:
        model = Centro
        fields = ['nombre', 'municipio', 'date_created', 'date_modified']