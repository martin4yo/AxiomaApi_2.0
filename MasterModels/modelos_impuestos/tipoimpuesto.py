from django.db import models
from ..universal import AuditModel
from .clasificacionimpuesto import ClasificacionImpuesto

class TipoImpuesto(AuditModel):
    """ Tipos de Impuestos """
    
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    idclasificacionimpuesto = models.ForeignKey(ClasificacionImpuesto, on_delete=models.CASCADE, related_name='clasificacionimpuesto_tipoimpuesto')
    
    class Meta:
        unique_together = (("codigo"),)
        verbose_name = 'Tipo de Impuesto'
        verbose_name_plural = 'IMPU - Tipos de Impuesto'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.idclasificacionimpuesto}'