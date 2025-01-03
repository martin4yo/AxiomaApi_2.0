from django.db import models
from ..universal import AuditModel

class TipoSujeto(AuditModel):
    """ Clase para manejar los tipos de sujeto """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Sujeto'
        verbose_name_plural = 'IMPU - Tipos de Sujeto'

    def __str__(self):
        return f'{self.nombre}' 