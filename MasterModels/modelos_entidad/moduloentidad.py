from django.db import models
from ..universal import AuditModel, TenantModel

class ModuloEntidad(AuditModel, TenantModel):
    """ Modulos por Entidad """
    
    identidad = models.ForeignKey('Entidad', related_name='entidad_modulo', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE, related_name='modulo_entidadmodulo')
               
    class Meta:
        unique_together = (("identidad", "idmodulo"),)
        verbose_name = 'Modulo por Entidad'
        verbose_name_plural = 'ENTI - Modulos por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}'