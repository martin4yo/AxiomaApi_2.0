from django.db import models
from ..universal import AuditModel, TenantModel 

class AtributoProducto(AuditModel, TenantModel):
    """ Clase para manejar los Atributos de Productos """

    idatributovalor = models.ForeignKey('AtributoValor', related_name='producto_atributovalor', on_delete=models.CASCADE)
    idproducto = models.ForeignKey('Producto', related_name='producto_atributo', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (("tenant_id", "idatributovalor","idproducto"),)
        verbose_name = 'Producto por Atributo'
        verbose_name_plural = 'ARTI - Producto por Atributo'

    def __str__(self):
        return f'{self.idatributovalor}, {self.idproducto}'
    