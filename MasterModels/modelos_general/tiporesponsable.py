from django.db import models
from ..universal import AuditModel, TenantModel

    
class TipoResponsable(AuditModel):
    """ Clase para manejar los tipos de responsable """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    sigla = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Responsable'
        verbose_name_plural = 'GRAL - Tipos de Responsable'

    def __str__(self):
        return f'{self.nombre}' 