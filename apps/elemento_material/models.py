from django.db import models
from apps.categoria_elemento.models import CategoriaElementos
from apps.tipo_elemento.models import TipoElemento
from django.db.models import SET_NULL

class ElementoMaterial(models.Model):
    #sitio =
    CodigoSena_Material = models.CharField(max_length=255)
    Categoria_Material = models.ForeignKey(CategoriaElementos, on_delete=SET_NULL, null=True)
    Tipo_Material = models.ForeignKey(TipoElemento, on_delete=SET_NULL, null=True)
    Nombre_Material = models.CharField(max_length=255)
    Descripcion_Material = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
    unidad_medida = models.CharField(max_length=255)
    producto_perecedero = models.BooleanField(default=False)
    FechaDevencimiento = models.DateTimeField(auto_created=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
