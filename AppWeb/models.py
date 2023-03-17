from django.db import models


class Home(models.Model):

    nombre = models.CharField(max_length=40)

