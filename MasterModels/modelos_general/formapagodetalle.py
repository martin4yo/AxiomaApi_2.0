from django.db import models
from ..universal import AuditModel, TenantModel

class FormaPagoDetalle(AuditModel, TenantModel):
    """ Clase para manejar los datos de paises """
    cuota = models.IntegerField()
    dias = models.IntegerField()
    nombre = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    idformapago = models.ForeignKey('FormaPago', on_delete=models.CASCADE, related_name='formapago_detalle')

    class Meta:
        verbose_name = 'Forma de Pago - Detalle'
        verbose_name_plural = 'GRAL - Formas de Pago - Detalle'

    def __str__(self):
        return f'{self.idformapago} - {self.dias}, {self.porcentaje}'