from django.db import models
from ..universal import AuditModel, TenantModel

class TipoFrecuencia(AuditModel):
    """ Clase para manejar los tipos de frecuencia """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Frecuencia'
        verbose_name_plural = 'GRAL - Tipos de Frecuencia'

    def __str__(self):
        return f'{self.nombre}' 
    