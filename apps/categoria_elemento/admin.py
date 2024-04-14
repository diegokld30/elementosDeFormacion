from django.contrib import admin
from apps.categoria_elemento.models import CategoriaElementos

# Register your models here.
@admin.register(CategoriaElementos)
class CategoriaElementosAdmin(admin.ModelAdmin):
    list_display = ['CodigoUNPSC_Material', 'Nombre_Categoria', 'date_created', 'date_modified']