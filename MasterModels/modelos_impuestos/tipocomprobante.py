from django.db import models
from ..universal import AuditModel

class TipoComprobante(AuditModel):
    """ Clase para manejar tipos de comprobante  """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    es_credito = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tipo de Comprobante'
        verbose_name_plural = 'IMPU - Tipos de Comprobante'

    def __str__(self):
        return f'{self.nombre}' 