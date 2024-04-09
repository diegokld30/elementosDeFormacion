from django.contrib import admin
from roles.models import Rol

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ['name_rol', 'state_rol', 'description']

