from django.db import models
from ..universal import AuditModel, TenantModel

class CondicionCrediticiaEntidad(AuditModel, TenantModel):
    """ Padrones de Impuesto """

    identidad = models.ForeignKey('Entidad', related_name='entidad_condicioncrediticia', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE, related_name='modulo_condicioncrediticia')
    vigenciadesde = models.DateField(null=False)
    vigenciahasta = models.DateField(null=False)
    limitedesde = models.DecimalField(max_digits=18, decimal_places=2)
    limitehasta = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        verbose_name = 'Condicion Crediticia'
        verbose_name_plural = 'ENTI - Condiciones Crediticias'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}, {self.vigenciadesde}, {self.limitedesde}'
    
