from django.db import models
from ..universal import AuditModel, TenantModel

class Mascara(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)
    estructura = models.CharField(max_length=256, default='')

    class Meta:
        verbose_name = 'Mascara'
        verbose_name_plural = 'GRAL - Mascaras'

    def __str__(self):
        return f'{self.nombre}' 

