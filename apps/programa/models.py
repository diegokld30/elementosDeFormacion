from django.db import models

# Create your models here.

class Programa(models.Model):
    nombre_programa = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre_programa
