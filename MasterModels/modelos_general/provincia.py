from django.db import models
from ..universal import AuditModel, TenantModel

class Provincia(AuditModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    idpais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    jurisdiccion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'GRAL - Provincias'

    def __str__(self):
        return f'{self.nombre}'


