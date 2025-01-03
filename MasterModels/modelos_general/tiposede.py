from django.db import models
from ..universal import AuditModel, TenantModel

class TipoSede(AuditModel, TenantModel):
    """ Clase para manejar los tipos de sedes """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Tipo de Sede'
        verbose_name_plural = 'GRAL - Tipos de Sede'

    def __str__(self):
        return f'{self.nombre}'