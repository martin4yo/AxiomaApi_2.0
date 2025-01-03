from django.db import models
from ..universal import AuditModel, TenantModel


class TipoDomicilio(AuditModel, TenantModel):
    """ Clase para manejar los tipos de domicilio """

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Tipo de Domicilio'
        verbose_name_plural = 'GRAL - Tipos de Domicilio'

    def __str__(self):
        return f'{self.nombre}'