from django.db import models
from ..universal import AuditModel, TenantModel

# ENTIDADES ########################################################################

""" Modelos para el modulo de entidades """

class Entidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    nombrefantasia = models.CharField(max_length=256, null=True, blank=True)
    nombre = models.CharField(max_length=256)
    codigo = models.CharField(max_length=20, null=True, blank=True)
    intercompany = models.BooleanField(default=False)
    idtiporesponsable = models.ForeignKey('TipoResponsable', on_delete=models.CASCADE, blank=True, null=True, related_name='tiporesponsable_entidad')
        
    class Meta:
        unique_together = (("tenant_id", "codigo"),)
        verbose_name = 'Entidad'
        verbose_name_plural = 'ENTI - Entidades'

    def __str__(self):
         return f'{self.codigo}, {self.nombrefantasia}, {self.nombre}'





    


       

    

