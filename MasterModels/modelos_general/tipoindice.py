from django.db import models
from ..universal import AuditModel, TenantModel

class TipoIndice(AuditModel):
    """ Tipos de Indice """
    
    nombre = models.CharField(max_length=100, default='a definir')
    codigo = models.CharField(max_length=10, unique=True)
    idmoneda = models.ForeignKey('Moneda', on_delete=models.CASCADE, related_name='moneda_tipoindice')
    idtipofrecuencia = models.ForeignKey('TipoFrecuencia', on_delete=models.CASCADE, related_name='tipofrecuencia_tipoindice')
    idtipovalor = models.ForeignKey('TipoValor', on_delete=models.CASCADE, related_name='tipovalor_tipoindice')
                                    
    class Meta:
        unique_together = (("codigo"),)
        verbose_name = 'Tipo de Indice'
        verbose_name_plural = 'GRAL - Tipos de Indice'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.idmoneda}'
    