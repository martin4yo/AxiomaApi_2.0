from django.db import models
from ..universal import AuditModel
from .tipoimpuesto import TipoImpuesto
from .alicuotaimpuesto import AlicuotaImpuesto
from .padronimpuesto import PadronImpuesto

class Impuesto(AuditModel):
    """ Impuestos """
    
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    calculapadron = models.BooleanField()
    idtipoimpuesto = models.ForeignKey(TipoImpuesto, on_delete=models.CASCADE, related_name='tipoimpuesto_impuesto')
    idalicuota = models.ForeignKey(AlicuotaImpuesto, on_delete=models.CASCADE, related_name='alicuota_impuesto')
    idpadron = models.ForeignKey(PadronImpuesto, on_delete=models.CASCADE, blank=True, null=True, related_name='padron_impuesto')
    idprovincia = models.ForeignKey('Provincia', on_delete=models.CASCADE, blank=True, null=True, related_name='provincia_impuesto')
    idpartido = models.ForeignKey('Partido', on_delete=models.CASCADE, blank=True, null=True, related_name='partido_impuesto')
    
    class Meta:
        unique_together = (("codigo"),)
        verbose_name = 'Impuesto'
        verbose_name_plural = 'IMPU - Impuestos'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.idtipoimpuesto}'