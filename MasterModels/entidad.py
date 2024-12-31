from django.db import models
from .universal import AuditModel, TenantModel


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

class CondicionCrediticiaEntidad(AuditModel, TenantModel):
    """ Padrones de Impuesto """

    identidad = models.ForeignKey('Entidad', related_name='entidad_condicioncrediticia', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE, related_name='modulo_condicioncrediticia')
    vigenciadesde = models.DateField(null=False)
    vigenciahasta = models.DateField(null=False)
    limitedesde = models.DecimalField(max_digits=18, decimal_places=2)
    limitehasta = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        verbose_name = 'Condicion Crediticia'
        verbose_name_plural = 'ENTI - Condiciones Crediticias'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}, {self.vigenciadesde}, {self.limitedesde}'
    
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
    
class Zona(AuditModel, TenantModel):
    """ Clase para manejar las zonas """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'GRAL - Zonas'

    def __str__(self):
        return f'{self.nombre}'

class EjecutivoEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', related_name='entidad_ejecutivo', on_delete=models.CASCADE)
    idpersona = models.ForeignKey('Persona', related_name='persona_ejecutivo', on_delete=models.CASCADE)
    idrol = models.ForeignKey('Rol', related_name='rol_ejecutivo', on_delete=models.CASCADE)
               
    class Meta:
        unique_together = (("identidad", "idpersona", "idrol"),)
        verbose_name = 'Ejecutivo'
        verbose_name_plural = 'ENTI - Ejecutivos'

    def __str__(self):
         return f'{self.identidad}, {self.idpersona}, {self.idrol}'
    
class DatosFiscalesEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', related_name = 'entidad_datosfiscales', on_delete=models.CASCADE)
    idtipodocumento = models.ForeignKey('TipoDocumento', on_delete=models.CASCADE, related_name='tipodocumento_datosfiscalesentidad')
    numerodocumento = models.CharField(max_length=100)
    idtiposujeto = models.ForeignKey('TipoSujeto', on_delete=models.CASCADE, related_name='tiposujeto_datosfiscalesentidad')
               
    class Meta:
        unique_together = (("identidad", "idtipodocumento", "numerodocumento"),)
        verbose_name = 'Datos Fiscales'
        verbose_name_plural = 'ENTI - Datos Fiscales por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idtipodocumento}, {self.numerodocumento}'
    
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
       
class ModuloEntidad(AuditModel, TenantModel):
    """ Modulos por Entidad """
    
    identidad = models.ForeignKey('Entidad', related_name='entidad_modulo', on_delete=models.CASCADE, null=True, blank=True)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE, related_name='modulo_entidadmodulo', null=True, blank=True)
               
    class Meta:
        unique_together = (("identidad", "idmodulo"),)
        verbose_name = 'Modulo por Entidad'
        verbose_name_plural = 'ENTI - Modulos por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}'
    
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
    