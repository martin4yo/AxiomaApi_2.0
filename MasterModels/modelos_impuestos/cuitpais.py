from django.db import models
from ..universal import AuditModel
from .tiposujeto import TipoSujeto

class CuitPais(AuditModel):
    """ Tipos de documento de CUIT de los paises """
    
    idtiposujeto = models.ForeignKey(TipoSujeto, on_delete=models.CASCADE, related_name='tiposujeto_cuitpais')
    nombre = models.CharField(max_length=256, default='')
    idtipodocumento = models.ForeignKey('TipoDocumento', on_delete=models.CASCADE, related_name='tipodocumento_cuitpais')
    idpais = models.ForeignKey('Pais', on_delete=models.CASCADE, related_name='pais_cuitpais')
    
    cuit = models.CharField(max_length=11, unique=True)

    class Meta:
        unique_together = (("cuit","idtiposujeto"),)
        verbose_name = 'CUIT Pais'
        verbose_name_plural = 'IMPU - Paises CUIT'

    def __str__(self):
         return f'{self.cuit},  {self.nombre}, {self.idtiposujeto}'