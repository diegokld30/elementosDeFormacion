from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

from users.api.forms import CustomUserCreationForm

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm


#@admin.register(User)
admin.site.register(User, CustomUserAdmin)
class UserAdmin(BaseUserAdmin):
    list_display = ['first_name', 'last_name', 'Cedula_persona', 'email','Rol_persona','Telefono_persona','Edad_persona']
    pass