from rest_framework.routers import DefaultRouter
from roles.api.views import RolApiViewSet

router_rol = DefaultRouter()
router_rol.register(prefix='rol', basename='rol', viewset=RolApiViewSet)