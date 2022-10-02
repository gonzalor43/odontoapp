from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length = 50, primary_key = True)
    contrasenia = models.CharField(max_length = 50)
    nombre_completo = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45, null = True)
    modif_fecha = models.DateTimeField(auto_now=True, null = True)
