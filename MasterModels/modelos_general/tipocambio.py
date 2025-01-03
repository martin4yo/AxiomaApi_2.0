from django.db import models
from ..universal import AuditModel, TenantModel

class TipoCambio(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    fecha = models.DateField()
    idmoneda = models.ForeignKey('Moneda', on_delete=models.CASCADE, related_name='moneda_tipocambio')
    importe = models.DecimalField(max_digits=18, decimal_places=2)
    vendedor = models.DecimalField(max_digits=18, decimal_places=2)
    comprador = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        unique_together = (("fecha","idmoneda"),)
        verbose_name = 'Tipo de Cambio'
        verbose_name_plural = 'GRAL - Tipos de Cambio'

    def __str__(self):
        return f'{self.idmoneda}, {self.fecha}, {self.importe}, {self.vendedor}, {self.comprador}' 

