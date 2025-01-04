from django.db import models
from ..universal import AuditModel, TenantModel 

class ContabilidadProducto(AuditModel, TenantModel):
    """ Clase para manejar las cuentas contables por producto """

    idproducto = models.ForeignKey('Producto', related_name='producto_contabilidad', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', related_name='contabilidadproducto_modulo', on_delete=models.CASCADE)
    idplancuenta = models.ForeignKey('PlanCuenta', related_name='contabilidadproducto_plancuenta', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("idproducto", "idmodulo"),)
        verbose_name = 'Cuenta Contable por Producto'
        verbose_name_plural = 'ARTI - Cuentas Contables por Producto'

    def __str__(self):
        return f'{self.idproducto}, {self.idmodulo}, {self.idplancuenta}'