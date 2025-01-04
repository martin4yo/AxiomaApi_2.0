from django.db import models
from ..universal import AuditModel, TenantModel 

class AtributoTipo(AuditModel, TenantModel):
    """ Clase para manejar los Productos """

    idatributo = models.ForeignKey('Atributo', related_name='atributotipo_atributo', on_delete=models.CASCADE)
    idtipoproducto = models.ForeignKey('TipoProducto', related_name='atributotipo_tipo', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (("tenant_id", "idatributo","idtipoproducto"),)
        verbose_name = 'Tipo de Producto por Atributo'
        verbose_name_plural = 'ARTI - Tipos de Producto por Atributo'

    def __str__(self):
        return f'{self.idatributo}, {self.idtipoproducto}'
    