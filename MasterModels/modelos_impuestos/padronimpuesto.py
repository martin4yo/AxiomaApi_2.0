from django.db import models
from ..universal import AuditModel

class PadronImpuesto(AuditModel):
    """ Padrones de Impuesto """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    porcentajedefecto = models.DecimalField(max_digits=5, decimal_places=2)
    tipocalculo = models.CharField(max_length=100, default='A DEFINIR...')

    class Meta:
        verbose_name = 'Padron'
        verbose_name_plural = 'IMPU - Padrones Impuesto'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.porcentaje}'