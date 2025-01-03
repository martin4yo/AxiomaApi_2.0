from django.db import models
from ..universal import AuditModel, TenantModel

class FormaPagoEntidad(AuditModel, TenantModel):
    """ Forma de Pago por Entidad """
    
    identidad = models.ForeignKey('Entidad', related_name='entidad_formapago', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE, related_name='modulo_formapagoentidad')
    idformapago = models.ForeignKey('FormaPago', on_delete=models.CASCADE, related_name='formapago_formapagoentidad')
               
    class Meta:
        unique_together = (("identidad", "idmodulo", "idformapago"),)
        verbose_name = 'Forma de Pago por Entidad'
        verbose_name_plural = 'ENTI - Forma de Pago por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}, {self.idformapago}'
    