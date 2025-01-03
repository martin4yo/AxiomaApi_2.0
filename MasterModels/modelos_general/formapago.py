from django.db import models
from ..universal import AuditModel, TenantModel

class FormaPago(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    habiles = models.BooleanField()

    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'GRAL - Formas de Pago'

    def __str__(self):
        return f'{self.nombre}' 

