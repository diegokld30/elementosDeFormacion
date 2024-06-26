from django.db import models

class TipoMovimiento(models.Model):
    tipo_movimiento = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo_movimiento