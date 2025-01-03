from django.db import models
from ..universal import AuditModel, TenantModel

class Indice(AuditModel, TenantModel):
    """ Valores de Indice """
    idtipoindice = models.ForeignKey('TipoIndice', on_delete=models.CASCADE, related_name='tipoindice_indice')
    desde = models.DateField()
    hasta = models.DateField()
    importe = models.DecimalField(max_digits=18, decimal_places=6, default=0)

    class Meta:
        unique_together = (("idtipoindice"),("desde"),("hasta"),)
        verbose_name = 'Indice'
        verbose_name_plural = 'GRAL - Indices'

    def __str__(self):
         return f'{self.idtipoindice}, {self.desde}, {self.hasta}, {self.importe}'
    