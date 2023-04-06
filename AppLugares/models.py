from django.db import models


class Post(models.Model):

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=30)
    lugar = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='Lugares/imagenes/')
    url = models.URLField(blank=True)


class Comentario(models.Model):

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=30)
    comentario = models.TextField()
    post_id = models.IntegerField()



