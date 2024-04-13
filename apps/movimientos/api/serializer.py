from rest_framework import serializers
from apps.movimientos.models import Movimiento
from apps.tipo_movimiento.api.serializers import TipoMovimientoSerializer
from apps.users.api.serializers import UserSerializer
from apps.movimientos.models import TipoMovimiento

class MovimientoSerializer(serializers.ModelSerializer):
    persona_movimiento = UserSerializer() #con esta linea se trae toda la informacion del usuario(persona_movimiento) que tenemos en la fk
    tipo_movimiento = TipoMovimientoSerializer()
    class Meta:
        model = Movimiento
        fields = ['id', 'tipo_movimiento', 'persona_movimiento', 'fecha_creacion', 'fecha_modificacion']
