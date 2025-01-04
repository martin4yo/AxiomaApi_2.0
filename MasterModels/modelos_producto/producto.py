from django.db import models
from ..universal import AuditModel, TenantModel 

class Producto(AuditModel, TenantModel):
    """ Clase para manejar los Productos """

    idtipoproducto = models.ForeignKey('TipoProducto', related_name='producto_tipoproducto', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=512)
    modificatexto = models.BooleanField(default=False)
    ean = models.CharField(max_length=20, blank=True)
    idunidadmedida = models.ForeignKey('UnidadMedida', related_name='producto_unidadmedida', on_delete=models.CASCADE)
    idclaseproducto = models.ForeignKey('ClaseProducto', related_name='producto_claseproducto', on_delete=models.CASCADE)
    decimales = models.IntegerField(default=2)
    stockminimo = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    stockmaximo = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    puntopedido = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    avisapedido = models.BooleanField(default=False)
    avisaminimo = models.BooleanField(default=False)
    preciocostopromedio = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    precioreferencia = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    precioultimacompra = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    preciocostostandard = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    
    class Meta:
        unique_together = (("tenant_id", "codigo"),)
        verbose_name = 'Producto'
        verbose_name_plural = 'ARTI - Productos'

    def __str__(self):
        return f'{self.tenant_id}, {self.codigo}, {self.nombre}'
    