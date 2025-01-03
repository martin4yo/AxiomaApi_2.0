from django.db import models
from ..universal import AuditModel, TenantModel

class Partido(AuditModel):
    """ Clase para manejar los datos de partidos """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    idprovincia = models.ForeignKey('Provincia', on_delete=models.CASCADE, related_name='provincia_partido')
    jurisdiccion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'GRAL - Partidos'

    def __str__(self):
        return f'{self.nombre}'

