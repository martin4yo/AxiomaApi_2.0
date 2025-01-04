from django.db import models
from ..universal import AuditModel, TenantModel

class PlanCuenta(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    nombre = models.CharField(max_length=256)
    codigo = models.CharField(max_length=20, unique=True)
    imputable = models.BooleanField(default=False)
    bimonetaria = models.BooleanField(default=False)
    idajustable = models.ForeignKey('TipoAjuste', on_delete=models.CASCADE, blank=True, null=True, related_name='tipoajuste_plancuentas')
    nivel = models.IntegerField()
    idpadre = models.ForeignKey('self', 
                                related_name="parents", 
                                on_delete=models.CASCADE, 
                                blank=True, null=True)
    
    class Meta:
        unique_together = (("codigo"),)
        verbose_name = 'Cuenta Contable'
        verbose_name_plural = 'CONT - Plan de Cuentas'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.idpadre}'
