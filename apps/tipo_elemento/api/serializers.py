from rest_framework import serializers
from apps.tipo_elemento.models import TipoElemento

class TipoElementoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoElemento
        fields = ['tipo_elemento', 'state', 'date_created', 'date_modified']

