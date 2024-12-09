"""
Modelos
"""
from django.utils import timezone
from django.db import models
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

# Clase general de auditoria #######################################################
"""
Modelo de datos para campos de auditoria
"""
class AuditModel(models.Model):
    """ Clase abstracta de auditoria para todas las clases """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)
    user_id = models.ForeignKey('Persona', on_delete=models.CASCADE)
    

    class Meta:
        """ Seteo de clase abstracta """
        abstract = True

class TenantModel(models.Model):
    tenant_id = models.CharField(max_length=50, default='')

    class Meta:
        abstract = True

# Generales ########################################################################

class TipoDeCambio(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    fecha = models.DateField()
    idmoneda = models.ForeignKey('Moneda', on_delete=models.CASCADE)
    importe = models.DecimalField(max_digits=18, decimal_places=2)
    vendedor = models.DecimalField(max_digits=18, decimal_places=2)
    comprador = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        unique_together = (("fecha","idmoneda"),)
        verbose_name = 'Tipo de Cambio'
        verbose_name_plural = 'GRAL - Tipos de Cambio'

    def __str__(self):
        return f'{self.idmoneda}, {self.fecha}, {self.importe}, {self.vendedor}, {self.comprador}' 

class FormaPago(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    habiles = models.BooleanField()

    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'GRAL - Formas de Pago'

    def __str__(self):
        return f'{self.nombre}' 

class FormaPagoDetalle(AuditModel, TenantModel):
    """ Clase para manejar los datos de paises """
    cuota = models.IntegerField()
    dias = models.IntegerField()
    nombre = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    idformapago = models.ForeignKey('FormaPago', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Forma de Pago - Detalle'
        verbose_name_plural = 'GRAL - Formas de Pago - Detalle'

    def __str__(self):
        return f'{self.idformapago} - {self.dias}, {self.porcentaje}'

class Mascara(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)
    estructura = models.CharField(max_length=256, default='')

    class Meta:
        verbose_name = 'Mascara'
        verbose_name_plural = 'GRAL - Mascaras'

    def __str__(self):
        return f'{self.nombre}' 

class Modulo(AuditModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Modulo'
        verbose_name_plural = 'GRAL - Modulos'

    def __str__(self):
        return f'{self.nombre}' 
    
class Rol(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'GRAL - Roles'

    def __str__(self):
        return f'{self.nombre}'  
    
class Sector(AuditModel, TenantModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'GRAL - Sectores'
  
    def __str__(self):
        return f'{self.nombre}' 
    
class Pais(AuditModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    codigoafip = models.CharField(max_length=10, unique=True)
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'GRAL - Paises'
  
    def __str__(self):
        return f'{self.nombre}'  

class Provincia(AuditModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    idpais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    jurisdiccion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'GRAL - Provincias'

    def __str__(self):
        return f'{self.nombre}'

class CodigoPostal(AuditModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    idpartido = models.ForeignKey('Partido', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Codigo Postal'
        verbose_name_plural = 'GRAL - Codigos Postales'

    def __str__(self):
        return f'{self.nombre}'
    
class Partido(AuditModel):
    """ Clase para manejar los datos de partidos """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    idprovincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)
    jurisdiccion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'GRAL - Partidos'

    def __str__(self):
        return f'{self.nombre}'

class Persona(models.Model):
    """ Clase para manejar los datos de una persona """
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)  # Considera usar un campo de contraseña más seguro
    mail = models.EmailField(max_length=254, unique=True)  # Agregando el campo mail
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)
    user_id = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'GRAL - Personas'

    def set_password(self, raw_password):
        """ Setea la password con seguridad """
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """ Valida el password con un metodo seguro """
        return check_password(raw_password, self.password)

    def __str__(self):
        return f'{self.nombre}'
    
class PersonaRol(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    idpersona = models.ForeignKey(Persona, related_name='roles', on_delete=models.CASCADE)
    idrol = models.ForeignKey('Rol', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("idpersona","idrol"),)
        verbose_name = 'Persona Roles'
        verbose_name_plural = 'GRAL - Personas Roles'

    def __str__(self):
        return f'{self.idpersona}, {self.idrol}' 
    
class TipoSede(AuditModel, TenantModel):
    """ Clase para manejar los tipos de sedes """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Tipo de Sede'
        verbose_name_plural = 'GRAL - Tipos de Sede'

    def __str__(self):
        return f'{self.nombre}'
    
class TipoDomicilio(AuditModel, TenantModel):
    """ Clase para manejar los tipos de domicilio """

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Tipo de Domicilio'
        verbose_name_plural = 'GRAL - Tipos de Domicilio'

    def __str__(self):
        return f'{self.nombre}'
    
class Idioma(AuditModel):
    """ Clase para manejar codigos de Idioma  """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'GRAL - Idioma'

    def __str__(self):
        return f'{self.nombre}' 
    
class Indice(AuditModel, TenantModel):
    """ Valores de Indice """
    idtipoindice = models.ForeignKey('TipoIndice', on_delete=models.CASCADE)
    desde = models.DateField()
    hasta = models.DateField()
    importe = models.DecimalField(max_digits=18, decimal_places=6, default=0)

    class Meta:
        unique_together = (("idtipoindice"),("desde"),("hasta"),)
        verbose_name = 'Indice'
        verbose_name_plural = 'GRAL - Indices'

    def __str__(self):
         return f'{self.idtipoindice}, {self.desde}, {self.hasta}, {self.importe}'
    
class Moneda(AuditModel):
    """ Clase para manejar monedas """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    afip = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Moneda'
        verbose_name_plural = 'GRAL - Monedas'

    def __str__(self):
        return f'{self.nombre}' 
    
class TipoDocumento(AuditModel):
    """ Tipos de documento de AFIP """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    codigoafip = models.CharField(max_length=10, unique=True)
    idmascara = models.ForeignKey(Mascara, on_delete=models.CASCADE)
    scriptvalidacion = models.TextField(default='')  # Valor por defecto como cadena vacía

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'GRAL - Tipos de Documento'

    def __str__(self):
         return f'{self.nombre}'
    
class TipoFrecuencia(AuditModel):
    """ Clase para manejar los tipos de frecuencia """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Frecuencia'
        verbose_name_plural = 'GRAL - Tipos de Frecuencia'

    def __str__(self):
        return f'{self.nombre}' 
    
class TipoIndice(AuditModel):
    """ Tipos de Indice """
    
    nombre = models.CharField(max_length=100, default='a definir')
    codigo = models.CharField(max_length=10, unique=True)
    idmoneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    idtipofrecuencia = models.ForeignKey('TipoFrecuencia', on_delete=models.CASCADE)
    idtipovalor = models.ForeignKey('TipoValor', on_delete=models.CASCADE)
                                    
    class Meta:
        unique_together = (("codigo"),)
        verbose_name = 'Tipo de Indice'
        verbose_name_plural = 'GRAL - Tipos de Indice'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.idmoneda}'
    
class TipoValor(AuditModel):
    """ Clase para manejar los tipos de valor """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Valor'
        verbose_name_plural = 'GRAL - Tipos de Valor'

    def __str__(self):
        return f'{self.nombre}' 
    
class UnidadMedida(AuditModel):
    """ Clase para manejar unidades de medida  """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    si = models.CharField(max_length=10, default='', unique=True)
    decimales = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'GRAL - Unidades de Medida'

    def __str__(self):
        return f'{self.nombre}' 
    
class Incoterms(AuditModel):
    """ Clase para manejar incoterms """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Incoterm'
        verbose_name_plural = 'GRAL - Incoterms'

    def __str__(self):
        return f'{self.codigo}' 
    
class TipoResponsable(AuditModel):
    """ Clase para manejar los tipos de responsable """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    sigla = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Responsable'
        verbose_name_plural = 'GRAL - Tipos de Responsable'

    def __str__(self):
        return f'{self.nombre}' 
       
# Impositivo ########################################################################

""" Modelos para el modulo impositivo """

class TipoComprobante(AuditModel):
    """ Clase para manejar tipos de comprobante  """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    es_credito = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tipo de Comprobante'
        verbose_name_plural = 'IMPU - Tipos de Comprobante'

    def __str__(self):
        return f'{self.nombre}' 

class ConceptoIncluido(AuditModel):
    """ Clase para manejar los conceptos a facturar segun AFIP """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Concepto Incluido'
        verbose_name_plural = 'IMPU - Conceptos Incluidos'

    def __str__(self):
        return f'{self.nombre}' 

class TipoSujeto(AuditModel):
    """ Clase para manejar los tipos de sujeto """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Sujeto'
        verbose_name_plural = 'IMPU - Tipos de Sujeto'

    def __str__(self):
        return f'{self.nombre}' 
    
class CuitPais(AuditModel):
    """ Tipos de documento de CUIT de los paises """
    
    idtiposujeto = models.ForeignKey(TipoSujeto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=256, default='')
    idmascara = models.ForeignKey(Mascara, on_delete=models.CASCADE)
    
    cuit = models.CharField(max_length=11, unique=True)

    class Meta:
        unique_together = (("cuit","idtiposujeto"),)
        verbose_name = 'CUIT Pais'
        verbose_name_plural = 'IMPU - Paises CUIT'

    def __str__(self):
         return f'{self.cuit},  {self.nombre}, {self.idtiposujeto}'
      
class AlicuotaImpuesto(AuditModel):
    """ Alicuotas de AFIP """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    codigofiscal = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Alicuota'
        verbose_name_plural = 'IMPU - Alicuotas Impuestos'

    def __str__(self):
         return f'{self.nombre}, {self.porcentaje}'
    
class PadronImpuesto(AuditModel):
    """ Padrones de Impuesto """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    porcentajedefecto = models.DecimalField(max_digits=5, decimal_places=2)
    tipocalculo = models.CharField(max_length=100, default='A DEFINIR...')

    class Meta:
        verbose_name = 'Padron'
        verbose_name_plural = 'IMPU - Padrones Impuesto'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.porcentaje}'
      
class TipoCalculo(AuditModel):
    """ Clase para manejar los tipos de calculo """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Calculo'
        verbose_name_plural = 'IMPU - Tipos de Calculo'

    def __str__(self):
        return f'{self.nombre}' 
    
class ClasificacionImpuesto(AuditModel):
    """ Clase para manejar los tipos de calculo """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Clasificacion Impuesto'
        verbose_name_plural = 'IMPU - Clasificaciones de Impuestos'

    def __str__(self):
        return f'{self.nombre}' 
    
class TipoImpuesto(AuditModel):
    """ Tipos de Impuestos """
    
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    idclasificacionimpuesto = models.ForeignKey(ClasificacionImpuesto, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (("codigo"),)
        verbose_name = 'Tipo de Impuesto'
        verbose_name_plural = 'IMPU - Tipos de Impuesto'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.idclasificacionimpuesto}'
    
class Impuesto(AuditModel):
    """ Impuestos """
    
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    calculapadron = models.BooleanField()
    idtipoimpuesto = models.ForeignKey(TipoImpuesto, on_delete=models.CASCADE)
    idalicuota = models.ForeignKey(AlicuotaImpuesto, on_delete=models.CASCADE)
    idplancuenta = models.ForeignKey('PlanCuentas', on_delete=models.CASCADE)
    idpadron = models.ForeignKey(PadronImpuesto, on_delete=models.CASCADE, blank=True, null=True)
    idprovincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, blank=True, null=True)
    idpartido = models.ForeignKey(Partido, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        unique_together = (("codigo"),)
        verbose_name = 'Impuesto'
        verbose_name_plural = 'IMPU - Impuestos'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.idtipoimpuesto}'
    
# CONTABILIDAD ########################################################################

""" Modelos para el modulo contable """

class TipoAjuste(AuditModel, TenantModel):
    """ Clase para manejar los tipos de sujeto """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=1, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Ajuste'
        verbose_name_plural = 'CONT - Tipos de Ajuste Contable'

    def __str__(self):
        return f'{self.nombre}'

class PlanCuentas(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    nombre = models.CharField(max_length=256)
    codigo = models.CharField(max_length=20, unique=True)
    imputable = models.BooleanField(default=False)
    bimonetaria = models.BooleanField(default=False)
    idajustable = models.ForeignKey('TipoAjuste', on_delete=models.CASCADE, blank=True, null=True)
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


# ENTIDADES ########################################################################

""" Modelos para el modulo de entidades """

class Entidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    nombrefantasia = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    codigo = models.CharField(max_length=20, unique=True)
    intercompany = models.BooleanField(default=False)
    idtiporesponsable = models.ForeignKey('TipoResponsable', on_delete=models.CASCADE, blank=True, null=True)
        
    class Meta:
        unique_together = (("codigo"),)
        verbose_name = 'Entidad'
        verbose_name_plural = 'ENTI - Entidades'

    def __str__(self):
         return f'{self.codigo}, {self.nombrefantasia}, {self.nombre}'

class CondicionCrediticia(AuditModel, TenantModel):
    """ Padrones de Impuesto """

    identidad = models.ForeignKey('Entidad', related_name='condicionescrediticias', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE)
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

    identidad = models.ForeignKey('Entidad', related_name = 'impuestos', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE)
    idimpuesto = models.ForeignKey('Impuesto', on_delete=models.CASCADE)
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

class Ejecutivo(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', related_name='ejecutivos', on_delete=models.CASCADE)
    idpersona = models.ForeignKey('Persona', related_name='personas', on_delete=models.CASCADE)
    idrol = models.ForeignKey('Rol', related_name='roles', on_delete=models.CASCADE)
               
    class Meta:
        unique_together = (("identidad", "idpersona", "idrol"),)
        verbose_name = 'Ejecutivo'
        verbose_name_plural = 'ENTI - Ejecutivos'

    def __str__(self):
         return f'{self.identidad}, {self.idpersona}, {self.idrol}'
    
class DatosFiscalesEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', related_name = 'datosfiscales', on_delete=models.CASCADE)
    idtipodocumento = models.ForeignKey('TipoDocumento', on_delete=models.CASCADE)
    numerodocumento = models.CharField(max_length=100)
    idtiposujeto = models.ForeignKey('TipoSujeto', on_delete=models.CASCADE)
               
    class Meta:
        unique_together = (("identidad", "idtipodocumento", "numerodocumento"),)
        verbose_name = 'Datos Fiscales'
        verbose_name_plural = 'ENTI - Datos Fiscales por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idtipodocumento}, {self.numerodocumento}'
    
class ContactoEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', related_name='contactos', on_delete=models.CASCADE)
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
    
    identidad = models.ForeignKey('Entidad', related_name='direcciones', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, unique=True)
    idtiposede = models.ForeignKey('TipoSede', on_delete=models.CASCADE)
    idtipodomicilio = models.ForeignKey('TipoDomicilio', on_delete=models.CASCADE)
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=50)
    piso = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    idpais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    idprovincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)
    idpartido = models.ForeignKey('Partido', on_delete=models.CASCADE)
    idcodigopostal = models.ForeignKey('CodigoPostal', on_delete=models.CASCADE)
    idzona = models.ForeignKey('Zona', on_delete=models.CASCADE)
    diasentrega = models.CharField(max_length=200)
    diasretiro = models.CharField(max_length=200)
               
    class Meta:
        unique_together = (("identidad", "nombre"),)
        verbose_name = 'Direccion Entidad'
        verbose_name_plural = 'ENTI - Direcciones de Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.nombre}, {self.idtiposede}'
       
class ModuloEntidad(AuditModel, TenantModel):
    """ Modulos por Entidad """
    
    identidad = models.ForeignKey('Entidad', related_name='modulos', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE)
               
    class Meta:
        unique_together = (("identidad", "idmodulo"),)
        verbose_name = 'Modulo por Entidad'
        verbose_name_plural = 'ENTI - Modulos por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}'
    
class SectorEntidad(AuditModel, TenantModel):
    """ Sectores por Entidad """
    
    identidad = models.ForeignKey('Entidad', related_name='sectores', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE)
    idsector = models.ForeignKey('Sector', on_delete=models.CASCADE)
               
    class Meta:
        unique_together = (("identidad", "idmodulo", "idsector"),)
        verbose_name = 'Sector por Entidad'
        verbose_name_plural = 'ENTI - Sectores por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}, {self.idsector}'
    
class FormaPagoEntidad(AuditModel, TenantModel):
    """ Forma de Pago por Entidad """
    
    identidad = models.ForeignKey('Entidad', related_name='formaspago', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE)
    idformapago = models.ForeignKey('FormaPago', on_delete=models.CASCADE)
               
    class Meta:
        unique_together = (("identidad", "idmodulo", "idformapago"),)
        verbose_name = 'Forma de Pago por Entidad'
        verbose_name_plural = 'ENTI - Forma de Pago por Entidad'

    def __str__(self):
         return f'{self.identidad}, {self.idmodulo}, {self.idformapago}'
    
       
# PRODUCTOS ########################################################################

""" Modelos para el modulo de productos """

class ListaPrecios(AuditModel, TenantModel):
    """ Clase para manejar los tipos de sujeto """

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Lista de Precios'
        verbose_name_plural = 'ARTI - Listas de Precio'

    def __str__(self):
        return f'{self.nombre}'
    
class ListaPrecioEntidad(AuditModel, TenantModel):
    """ Plan de Cuentas """
    
    identidad = models.ForeignKey('Entidad', on_delete=models.CASCADE)
    idmodulo = models.ForeignKey('Modulo', on_delete=models.CASCADE)
    idlistaprecio = models.ForeignKey('ListaPrecios', on_delete=models.CASCADE)
               
    class Meta:
        unique_together = (("identidad", "idmodulo", "idlistaprecio"),)
        verbose_name = 'Listas de Precio'
        verbose_name_plural = 'ARTI - Listas de Precio por Entidad'