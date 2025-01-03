from django.db import models
from ..universal import AuditModel, TenantModel

class EjecutivoEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', related_name='entidad_ejecutivo', on_delete=models.CASCADE)
    idpersona = models.ForeignKey('Persona', related_name='persona_ejecutivo', on_delete=models.CASCADE)
    idrol = models.ForeignKey('Rol', related_name='rol_ejecutivo', on_delete=models.CASCADE)
               
    class Meta:
        unique_together = (("identidad", "idpersona", "idrol"),)
        verbose_name = 'Ejecutivo'
        verbose_name_plural = 'ENTI - Ejecutivos'

    def __str__(self):
         return f'{self.identidad}, {self.idpersona}, {self.idrol}'
    