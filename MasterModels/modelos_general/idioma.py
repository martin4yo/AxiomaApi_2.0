from django.db import models
from ..universal import AuditModel, TenantModel

class Idioma(AuditModel):
    """ Clase para manejar codigos de Idioma  """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'GRAL - Idioma'

    def __str__(self):
        return f'{self.nombre}' 
    
