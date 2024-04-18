from rest_framework import serializers
from apps.area_sede.models import AreaSede
from apps.sede.api.serializers import SedeSerializer
from apps.area.api.serializers import AreaSerializer
from apps.users.api.serializers import UserSerializer

class AreaSedeSerializer(serializers.ModelSerializer):
    sede_area = SedeSerializer
    area_AreaSede = AreaSerializer
    persona_administra = UserSerializer
    class Meta:
        model = AreaSede
        fields = ['sede_area', 'area_AreaSede', 'persona_administra', 'date_created', 'date_modified']
