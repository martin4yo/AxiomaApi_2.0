from django.db import models
from ..universal import AuditModel

class ClasificacionImpuesto(AuditModel):
    """ Clase para manejar los tipos de calculo """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Clasificacion Impuesto'
        verbose_name_plural = 'IMPU - Clasificaciones de Impuestos'

    def __str__(self):
        return f'{self.nombre}' 