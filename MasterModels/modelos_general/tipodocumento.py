from django.db import models
from ..universal import AuditModel, TenantModel

class TipoDocumento(AuditModel):
    """ Tipos de documento de AFIP """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    codigoISO = models.CharField(max_length=10, unique=True)
    idmascara = models.ForeignKey('Mascara', on_delete=models.CASCADE, related_name='mascara_tipodocumento')
    scriptvalidacion = models.TextField(default='')  # Valor por defecto como cadena vacía

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'GRAL - Tipos de Documento'

    def __str__(self):
         return f'{self.nombre}'
    