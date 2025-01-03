from django.db import models
from ..universal import AuditModel, TenantModel

class DireccionEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', related_name='entidad_direccion', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    idtiposede = models.ForeignKey('TipoSede', on_delete=models.CASCADE, related_name='tiposede_direcciones')
    idtipodomicilio = models.ForeignKey('TipoDomicilio', on_delete=models.CASCADE, related_name='tipodomicilio_direcciones')
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=50)
    piso = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    idpais = models.ForeignKey('Pais', on_delete=models.CASCADE, related_name='pais_direcciones')
    idprovincia = models.ForeignKey('Provincia', on_delete=models.CASCADE, related_name='provincia_direcciones')
    idpartido = models.ForeignKey('Partido', on_delete=models.CASCADE, related_name='partido_direcciones')
    idcodigopostal = models.ForeignKey('CodigoPostal', on_delete=models.CASCADE, related_name='codigopostal_direcciones')
    idzona = models.ForeignKey('Zona', on_delete=models.CASCADE, related_name='zona_direcciones')
    diasentrega = models.CharField(max_length=200, blank=True, null=True)
    diasretiro = models.CharField(max_length=200, blank=True, null=True)
               
    class Meta:
        unique_together = (("identidad", "nombre"),)
        verbose_name = 'Direccion Entidad'
        verbose_name_plural = 'ENTI - Direcciones de Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.nombre}, {self.idtiposede}'