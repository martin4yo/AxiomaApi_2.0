from django.db import models
from ..universal import AuditModel, TenantModel

class DatosFiscalesEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', related_name = 'entidad_datosfiscales', on_delete=models.CASCADE)
    idtipodocumento = models.ForeignKey('TipoDocumento', on_delete=models.CASCADE, related_name='tipodocumento_datosfiscalesentidad')
    numerodocumento = models.CharField(max_length=100)
    idtiposujeto = models.ForeignKey('TipoSujeto', on_delete=models.CASCADE, related_name='tiposujeto_datosfiscalesentidad')
               
    class Meta:
        unique_together = (("identidad", "idtipodocumento", "numerodocumento"),)
        verbose_name = 'Datos Fiscales'
        verbose_name_plural = 'ENTI - Datos Fiscales por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idtipodocumento}, {self.numerodocumento}'