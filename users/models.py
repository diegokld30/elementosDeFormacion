from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import SET_NULL
from roles.models import Rol
class User(AbstractUser):

    Cedula_persona = models.CharField(max_length=255, blank=True)
    Edad_persona = models.CharField(max_length=100)
    Telefono_persona = models.CharField(max_length=255)
    Rol_persona = models.ForeignKey(Rol, on_delete=SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    # Con esto se configura que se debe iniciar sesion con el email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []