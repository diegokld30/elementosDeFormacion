from rest_framework.routers import DefaultRouter
from movimientos.api.views import MovimientoApiViewSet

router_movimiento = DefaultRouter()
router_movimiento.register(prefix='movimiento', basename='movimiento', viewset=MovimientoApiViewSet)