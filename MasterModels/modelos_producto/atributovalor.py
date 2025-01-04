from django.db import models
from ..universal import AuditModel, TenantModel 

class AtributoValor(AuditModel, TenantModel):
    """ Clase para manejar los Productos """

    idatributo = models.ForeignKey('Atributo', related_name='atributovalor_atributo', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=512)
    
    class Meta:
        unique_together = (("tenant_id", "idatributo","codigo"),)
        verbose_name = 'Valor de Atributo'
        verbose_name_plural = 'ARTI - Valores de Atributos'

    def __str__(self):
        return f'{self.codigo}, {self.nombre}, {self.idatributo}'
    