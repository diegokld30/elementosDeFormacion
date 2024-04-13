from django.db import models
from django.db.models import SET_NULL
from apps.users.models import User

# Create your models here.

class Movimiento(models.Model):
    tipo_movimiento = models.CharField(max_length=255)
    #slug = models.SlugField(max_length=255, unique=True) aca no me sirve por que los tipos de movimiento siempre son los mismos
    persona_movimiento = models.ForeignKey(User, on_delete=SET_NULL, null=True) #si se elimina el usuarios no se eliminara el movimiento, solo se pondra este espacio en null
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    #pendiente por crear ls fk de tipo de movimiento

