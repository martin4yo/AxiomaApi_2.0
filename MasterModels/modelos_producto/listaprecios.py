from django.db import models
from ..universal import AuditModel, TenantModel


class ListaPrecios(AuditModel, TenantModel):
    """ Clase para manejar los tipos de sujeto """

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Lista de Precios'
        verbose_name_plural = 'ARTI - Listas de Precio'

    def __str__(self):
        return f'{self.nombre}'
    
