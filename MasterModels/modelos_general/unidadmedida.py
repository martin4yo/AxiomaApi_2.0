from django.db import models
from ..universal import AuditModel, TenantModel

class UnidadMedida(AuditModel):
    """ Clase para manejar unidades de medida  """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    si = models.CharField(max_length=10, default='', unique=True)
    decimales = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'GRAL - Unidades de Medida'

    def __str__(self):
        return f'{self.codigo}, {self.nombre}' 