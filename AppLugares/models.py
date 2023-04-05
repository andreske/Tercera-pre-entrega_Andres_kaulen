from django.db import models


class Post(models.Model):

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    lugar = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='Lugares/imagenes/')
    url = models.URLField(blank=True)
