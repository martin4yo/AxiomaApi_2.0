from django.db import models
from ..universal import AuditModel, TenantModel

class CodigoPostal(AuditModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    idpartido = models.ForeignKey('Partido', on_delete=models.CASCADE, related_name='partido_codigopostal')

    class Meta:
        verbose_name = 'Codigo Postal'
        verbose_name_plural = 'GRAL - Codigos Postales'

    def __str__(self):
        return f'{self.nombre}'
    