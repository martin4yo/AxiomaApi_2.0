from django.db import models
from django.utils.timezone import now
from ..universal import AuditModel, TenantModel

class ListaPrecio(AuditModel, TenantModel):
    """ Clase para manejar las listas de precio"""

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    incluyeimpuestos = models.BooleanField(default=False)
    vigenciadesde = models.DateField(null=False, blank=False)
    vigenciahasta = models.DateField(null=False, blank=False)
    idtipolista = models.ForeignKey('ListaTipo', related_name='lista_tipo', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("tenant_id", "codigo"),)
        verbose_name = 'Lista de Precios'
        verbose_name_plural = 'ARTI - Listas de Precio'

    def __str__(self):
        return f'{self.codigo}, {self.nombre}'
    
