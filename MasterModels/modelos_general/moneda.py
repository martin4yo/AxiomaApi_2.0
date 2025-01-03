from django.db import models
from ..universal import AuditModel, TenantModel

class Moneda(AuditModel):
    """ Clase para manejar monedas """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    afip = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Moneda'
        verbose_name_plural = 'GRAL - Monedas'

    def __str__(self):
        return f'{self.nombre}' 
    

