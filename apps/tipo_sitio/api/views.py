from rest_framework.viewsets import ModelViewSet

from apps.tipo_movimiento.api.serializers import TipoMovimientoSerializer
from apps.tipo_movimiento.models import TipoMovimiento

class TipoMovimientoViewSet(ModelViewSet):
    serializer_class = TipoMovimientoSerializer
    queryset = TipoMovimiento.objects.all()