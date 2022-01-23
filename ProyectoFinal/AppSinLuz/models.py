from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)

class Reclamo(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)


class Administrativo(models.Model):
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)