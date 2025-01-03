from django.db import models
from ..universal import AuditModel, TenantModel

class PersonaRol(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    idpersona = models.ForeignKey('Persona', related_name='roles', on_delete=models.CASCADE)
    idrol = models.ForeignKey('Rol', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("idpersona","idrol"),)
        verbose_name = 'Persona Roles'
        verbose_name_plural = 'GRAL - Personas Roles'

    def __str__(self):
        return f'{self.idpersona}, {self.idrol}' 
    


    
