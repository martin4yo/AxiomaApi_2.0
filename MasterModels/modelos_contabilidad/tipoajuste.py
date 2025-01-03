from django.db import models
from ..universal import AuditModel, TenantModel

# CONTABILIDAD ########################################################################

""" Modelos para el modulo contable """

class TipoAjuste(AuditModel, TenantModel):
    """ Clase para manejar los tipos de sujeto """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=1, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Ajuste'
        verbose_name_plural = 'CONT - Tipos de Ajuste Contable'

    def __str__(self):
        return f'{self.nombre}'
