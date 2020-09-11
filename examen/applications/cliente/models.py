from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    ape_paterno = models.CharField(max_length=50)
    ape_materno = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)

