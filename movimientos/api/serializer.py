from rest_framework import serializers
from movimientos.models import Movimiento

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = ['id', 'tipo_movimiento', 'persona_movimiento', 'fecha_creacion', 'fecha_modificacion']