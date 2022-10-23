from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    email_usuario = models.CharField(max_lenght=100)
    pass_usuario = models.CharField(min_lenght=6, max_lenght=20)
    