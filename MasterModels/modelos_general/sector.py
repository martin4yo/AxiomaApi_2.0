from django.db import models
from ..universal import AuditModel, TenantModel

class Sector(AuditModel, TenantModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'GRAL - Sectores'
  
    def __str__(self):
        return f'{self.nombre}' 
    
