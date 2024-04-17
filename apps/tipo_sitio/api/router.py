from rest_framework.routers import DefaultRouter
from apps.tipo_sitio.api.views import TipoMovimientoViewSet

router_tipoSitio = DefaultRouter()
router_tipoSitio.register(prefix='tipo_sitio', basename='tipo_sitio', viewset=TipoMovimientoViewSet)