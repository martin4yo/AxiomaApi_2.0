from django.db import models
from ..universal import AuditModel, TenantModel
    
class Zona(AuditModel, TenantModel):
    """ Clase para manejar las zonas """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'GRAL - Zonas'

    def __str__(self):
        return f'{self.nombre}'
