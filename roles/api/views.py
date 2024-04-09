from rest_framework.viewsets import ModelViewSet
from roles.models import Rol
from roles.api.serializer import RolSerializer
from roles.api.permissions import IsAdminOrReadOnly


class RolApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly] #Los permisos que se le dan para que muestre si es staff o no
    serializer_class = RolSerializer #Cosas que vamos a mostrar
    queryset = Rol.objects.all()
