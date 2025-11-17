from django.db import models
from app_Empresa.models import Empresa
from django.contrib.auth.models import User, Group

class Perfiluser(models.Model):
    imagen_url = models.URLField(
        max_length=200,
        blank=True,
        null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.empresa.razon_social}"


class GroupDescripcion(models.Model):
    """Modelo para almacenar la descripción de los grupos"""
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='descripcion_obj')
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.group.name} - {self.descripcion}"
