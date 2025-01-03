from django.db import models
from ..universal import AuditModel, TenantModel

class SectorEntidad(AuditModel, TenantModel):
    """ Sectores por Entidad """
    
    identidad = models.ForeignKey('Entidad', related_name='entidad_sector', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE, related_name='modulo_sectorentidad')
    idsector = models.ForeignKey('Sector', on_delete=models.CASCADE, related_name='sector_sectorentidad')
               
    class Meta:
        unique_together = (("identidad", "idmodulo", "idsector"),)
        verbose_name = 'Sector por Entidad'
        verbose_name_plural = 'ENTI - Sectores por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}, {self.idsector}'
    