from django.db import models
from ..universal import AuditModel, TenantModel 

class ConversionProducto(AuditModel, TenantModel):
    """ Clase para manejar las cuentas contables por producto """

    idproducto = models.ForeignKey('Producto', related_name='producto_conversion', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', related_name='conversionproducto_modulo', on_delete=models.CASCADE)
    idunidadmedida = models.ForeignKey('UnidadMedida', related_name='conversionproducto_unidadmedida', on_delete=models.CASCADE)
    factorconversion = models.DecimalField(max_digits=18, decimal_places=6)

    class Meta:
        unique_together = (("idproducto", "idmodulo", "idunidadmedida"),)
        verbose_name = 'Conversion por Producto'
        verbose_name_plural = 'ARTI - Conversiones por Producto'

    def __str__(self):
        return f'{self.idproducto}, {self.idmodulo}, {self.idunidadmedida}, {self.factorconversion}'
    