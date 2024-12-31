from django.db import models
from .universal import AuditModel, TenantModel
             
# PRODUCTOS ########################################################################

""" Modelos para el modulo de productos """

class ListaPrecios(AuditModel, TenantModel):
    """ Clase para manejar los tipos de sujeto """

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Lista de Precios'
        verbose_name_plural = 'ARTI - Listas de Precio'

    def __str__(self):
        return f'{self.nombre}'
    
class ListaPrecioEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', on_delete=models.CASCADE, related_name='entidad_listaprecioentidad')
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE, related_name='modulo_listaprecioentidad')
    idlistaprecio = models.ForeignKey('ListaPrecios', on_delete=models.CASCADE, related_name='listaprecios_listaprecioentidad')
               
    class Meta:
        unique_together = (("identidad", "idmodulo", "idlistaprecio"),)
        verbose_name = 'Listas de Precio'
        verbose_name_plural = 'ARTI - Listas de Precio por Entidad'