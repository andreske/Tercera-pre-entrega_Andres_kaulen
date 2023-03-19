from django.db import models


class Home(models.Model):

    nombre = models.CharField(max_length=30)


class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


class Solicitud(models.Model):

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    nombre_solicitud = models.CharField(max_length=50)
    cantidad = models.IntegerField()


class Direcciones(models.Model):

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    calle = models.CharField(max_length=30)
    numero = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)