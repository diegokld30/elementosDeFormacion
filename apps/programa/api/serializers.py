from rest_framework import serializers
from apps.programa.models import Programa
from apps.area.api.serializers import AreaSerializer

class ProgramaSerializer(serializers.ModelSerializer):
    area_programa = AreaSerializer()
    class Meta:
        model = Programa
        fields = ['nombre_programa', 'area_programa','date_created', 'date_modified']