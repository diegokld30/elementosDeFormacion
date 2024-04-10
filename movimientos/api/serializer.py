from rest_framework import serializers
from movimientos.models import Movimiento
from users.api.serializers import UserSerializer

class MovimientoSerializer(serializers.ModelSerializer):
    persona_movimiento = UserSerializer() #con esta linea se trae toda la informacion del usuario(persona_movimiento) que tenemos en la fk
    class Meta:
        model = Movimiento
        fields = ['id', 'tipo_movimiento', 'persona_movimiento', 'fecha_creacion', 'fecha_modificacion']
