from django.db import models


class Home(models.Model):
    pass


class About(models.Model):
    pass


class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Usuario: {self.nombre}, Apellido: {self.apellido}"


