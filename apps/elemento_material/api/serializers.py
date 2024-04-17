from rest_framework import serializers
from apps.elemento_material.models import ElementoMaterial
from apps.tipo_elemento.api.serializers import TipoElementoSerializer
from apps.categoria_elemento.api.serializers import CategoriaElementosSerializer
class ElementoMaterialSerializer(serializers.ModelSerializer):
    Categoria_Material = CategoriaElementosSerializer()
    Tipo_Material = TipoElementoSerializer()
    class Meta:

        model = ElementoMaterial

        fields = ['CodigoSena_Material', 'Categoria_Material', 'Tipo_Material','Nombre_Material','Tipo_Material','Nombre_Material','Descripcion_Material','stock', 'unidad_medida', 'producto_perecedero', 'FechaDevencimiento', 'date_created', 'date_modified']
