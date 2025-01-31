from django.db import models
from ..universal import AuditModel, TenantModel

class Precio(AuditModel, TenantModel):
    """ Clase para manejar las listas de precio"""

    idlistaprecio = models.ForeignKey('ListaPrecio', related_name='precio_lista', on_delete=models.CASCADE, blank=True)
    idproducto = models.ForeignKey('Producto', related_name='producto_precio', on_delete=models.CASCADE, blank=True)
    costo = models.DecimalField(max_digits=18, decimal_places=4, default=0)
    margen = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    precio = models.DecimalField(max_digits=18, decimal_places=4, default=0)

    class Meta:
        unique_together = (("tenant_id", "idlistaprecio","idproducto"),)
        verbose_name = 'Precio'
        verbose_name_plural = 'ARTI - Precios'

    def __str__(self):
        return f'{self.idlista.nombre}, {self.idproducto.nombre}, {self.costo}, {self.margen}, {self.precio}'
    
