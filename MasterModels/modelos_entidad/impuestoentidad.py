from django.db import models
from ..universal import AuditModel, TenantModel

class ImpuestoEntidad(AuditModel, TenantModel):
    """ Padrones de Impuesto por entidad """

    identidad = models.ForeignKey('Entidad', related_name = 'entidad_impuesto', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE, related_name='modulo_impuestoentidad')
    idimpuesto = models.ForeignKey('Impuesto', on_delete=models.CASCADE, related_name='impuesto_impuestoentidad')
    aplica = models.BooleanField()
    porcentajexencion = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
    resolucion = models.CharField(max_length=100, blank=True, null=True)
    vigenciadesde = models.DateField(blank=True,null=True)
    vigenciahasta = models.DateField(blank=True,null=True)

    class Meta:
        unique_together = (("identidad", "idmodulo", "idimpuesto"),)
        verbose_name = 'Impuesto por Entidad'
        verbose_name_plural = 'ENTI - Impuestos por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}, {self.idimpuesto}'