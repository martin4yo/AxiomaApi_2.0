from django.db import models
from ..universal import AuditModel

class ConceptoIncluido(AuditModel):
    """ Clase para manejar los conceptos a facturar segun AFIP """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Concepto Incluido'
        verbose_name_plural = 'IMPU - Conceptos Incluidos'

    def __str__(self):
        return f'{self.nombre}' 
