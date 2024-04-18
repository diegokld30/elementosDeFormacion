from rest_framework import serializers
from apps.ficha.models import Ficha
from apps.programa.api.serializers import ProgramaSerializer
from apps.users.api.serializers import UserSerializer

class FichaSerializer(serializers.ModelSerializer):
    persona_ficha = UserSerializer()
    programa = ProgramaSerializer()
    class Meta:
        model = Ficha
        fields = ['persona_ficha', 'programa', 'date_created', 'date_modified']