from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    nombre = models.CharField('Nombre', max_length=45)
    primer_apellido = models.CharField('Primer apellido', max_length=35)
    segundo_apellido = models.CharField(
        'Segundo apellido', max_length=35, null=True, blank=True)
    user = models.CharField('Usuario', max_length=20)
    contra = models.CharField('Contraseña', max_length=20, default=None)
