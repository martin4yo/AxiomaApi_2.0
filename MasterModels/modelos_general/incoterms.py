from django.db import models
from ..universal import AuditModel, TenantModel

class Incoterms(AuditModel):
    """ Clase para manejar incoterms """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Incoterm'
        verbose_name_plural = 'GRAL - Incoterms'

    def __str__(self):
        return f'{self.codigo}' 
