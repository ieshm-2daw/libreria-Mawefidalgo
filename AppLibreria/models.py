from django.db import models

# Create your models here.
class ModeloLibreria(models.Model):
    dni = models.CharField
    direccion = models.TextField
    telefono = models.IntegerField

    def __str__(self):
        return self.dni