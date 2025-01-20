from django.db import models
from ..universal import AuditModel, TenantModel

class ListaPrecioEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', on_delete=models.CASCADE, related_name='entidad_lista')
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE, related_name='modulo_listaprecioentidad')
    idlistaprecio = models.ForeignKey('ListaPrecio', on_delete=models.CASCADE, related_name='listaprecios_listaprecioentidad')
               
    class Meta:
        unique_together = (("identidad", "idmodulo", "idlistaprecio"),)
        verbose_name = 'Listas de Precio'
        verbose_name_plural = 'ARTI - Listas de Precio por Entidad'