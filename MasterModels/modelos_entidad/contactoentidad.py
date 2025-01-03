from django.db import models
from ..universal import AuditModel, TenantModel

class ContactoEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', related_name='entidad_contacto', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
               
    class Meta:
        unique_together = (("identidad", "nombre"),)
        verbose_name = 'Contacto Entidad'
        verbose_name_plural = 'ENTI - Contactos Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.nombre}, {self.rol}'
    