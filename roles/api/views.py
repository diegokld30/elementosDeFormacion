from rest_framework.viewsets import ModelViewSet
from roles.models import Rol
from roles.api.serializer import RolSerializer


class RolApiViewSet(ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()
