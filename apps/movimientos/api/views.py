from rest_framework.viewsets import ModelViewSet
from apps.movimientos.models import Movimiento
from apps.movimientos.api.serializer import MovimientoSerializer
from apps.movimientos.api.permissions import IsAdminOrReadOnly

class MovimientoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]#Con esto estoy diciendo que debe ser staff para poder hacer cualquier cosa que nosea GET
    serializer_class = MovimientoSerializer
    queryset = Movimiento.objects.all()