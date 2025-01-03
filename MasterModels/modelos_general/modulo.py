from django.db import models
from ..universal import AuditModel, TenantModel

class Modulo(AuditModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Modulo'
        verbose_name_plural = 'GRAL - Modulos'

    def __str__(self):
        return f'{self.nombre}' 
    
