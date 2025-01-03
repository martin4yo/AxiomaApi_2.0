from django.db import models
from ..universal import AuditModel, TenantModel

class Rol(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'GRAL - Roles'

    def __str__(self):
        return f'{self.nombre}'  
    
