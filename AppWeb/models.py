from django.db import models


class Home(models.Model):

    nombre = models.CharField(max_length=40)


class Usuario(models.Model):

    nombre= models.CharField(max_lenght=30)
    apellido= models.CharField(max_lenght=30)
    email= models.EmailField()

class Solicitud(models.Model):

    cantidad= models.IntegerField()

class Direcciones(models.Model):

    nombre_pila=