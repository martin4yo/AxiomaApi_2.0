from django.db import models
from ..universal import AuditModel

class AlicuotaImpuesto(AuditModel):
    """ Alicuotas de AFIP """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    codigofiscal = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Alicuota'
        verbose_name_plural = 'IMPU - Alicuotas Impuestos'

    def __str__(self):
         return f'{self.nombre}, {self.porcentaje}'
    