from django.db import models
from ..universal import AuditModel, TenantModel

class Pais(AuditModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    codigoISO = models.CharField(max_length=10, unique=True)
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'GRAL - Paises'
  
    def __str__(self):
        return f'{self.nombre}'  

