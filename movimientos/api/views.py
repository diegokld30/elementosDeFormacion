from rest_framework.viewsets import ModelViewSet
from movimientos.models import Movimiento
from movimientos.api.serializer import MovimientoSerializer

class MovimientoApiViewSet(ModelViewSet):
    serializer_class = MovimientoSerializer
    queryset = Movimiento.objects.all()