# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario
