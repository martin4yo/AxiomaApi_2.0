from django.db import models
from ..universal import AuditModel, TenantModel 

class ListaTipo(AuditModel, TenantModel):
    """ Clase para manejar los tipos de producto """
    
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    class Meta:
        unique_together = (("tenant_id", "codigo"),)
        verbose_name = 'Tipo de Lista de Precios'
        verbose_name_plural = 'ARTI - Tipos de Listas de Precio'

    def __str__(self):
        return f'{self.codigo}, {self.nombre}'
    
    