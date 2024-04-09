from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #Con esto se configura que se debe iniciar sesion con le email
    Cedula_persona = models.CharField(max_length=255, blank=True)
    Edad_persona = models.CharField(max_length=100)
    Telefono_persona = models.CharField(max_length=255)
    Rol_persona = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []