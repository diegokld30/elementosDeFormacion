from rest_framework import serializers
from apps.programa.models import Programa

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ['nombre_programa', 'date_created', 'date_modified']