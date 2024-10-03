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

# Generales ########################################################################

class TipoDeCambio(AuditModel):
    """ Clase para manejar los roles """
    fecha = models.DateField()
    idmoneda = models.ForeignKey('Moneda', on_delete=models.CASCADE)
    importe = models.DecimalField(max_digits=18, decimal_places=2)
    vendedor = models.DecimalField(max_digits=18, decimal_places=2)
    comprador = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        unique_together = (("fecha","idmoneda"),)
        verbose_name = 'Tipo de Cambio'
        verbose_name_plural = 'Tipos de Cambio'

    def __str__(self):
        return f'{self.idmoneda}, {self.fecha}, {self.importe}, {self.vendedor}, {self.comprador}' 

class FormaDePago(AuditModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de Pago'

    def __str__(self):
        return f'{self.nombre}' 

class FormaDePagoDetalle(AuditModel):
    """ Clase para manejar los datos de paises """
    dias = models.IntegerField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    idformadepago = models.ForeignKey('FormaDePago', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Forma de Pago - Detalle'
        verbose_name_plural = 'Formas de Pago - Detalle'

    def __str__(self):
        return f'{self.idformadepago} - {self.dias}, {self.porcentaje}'

class Mascara(AuditModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)
    estructura = models.CharField(max_length=256, default='')

    class Meta:
        verbose_name = 'Mascara'
        verbose_name_plural = 'Mascaras'

    def __str__(self):
        return f'{self.nombre}' 

class Modulo(AuditModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'

    def __str__(self):
        return f'{self.nombre}' 
    
class Rol(AuditModel):
    """ Clase para manejar los roles """
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return f'{self.nombre}'  
    
class Pais(AuditModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
  
    def __str__(self):
        return f'{self.nombre}'  

class Provincia(AuditModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    idpais = models.ForeignKey('Pais', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return f'{self.nombre}'

class CodigoPostal(AuditModel):
    """ Clase para manejar los datos de paises """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    idprovincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Codigo Postal'
        verbose_name_plural = 'Codigos Postales'

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
        verbose_name_plural = 'Personas'

    def set_password(self, raw_password):
        """ Setea la password con seguridad """
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """ Valida el password con un metodo seguro """
        return check_password(raw_password, self.password)

    def __str__(self):
        return f'{self.nombre}'
    
class PersonaRol(AuditModel):
    """ Clase para manejar los roles """
    idpersona = models.ForeignKey(Persona, related_name='roles', on_delete=models.CASCADE)
    idrol = models.ForeignKey('Rol', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("idpersona","idrol"),)
        verbose_name = 'Persona Roles'
        verbose_name_plural = 'Personas Roles'

    def __str__(self):
        return f'{self.idpersona}, {self.idrol}' 
    
# Impositivo ########################################################################

""" Modelos para el modulo impositivo """

class Moneda(AuditModel):
    """ Clase para manejar monedas """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    sigla = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Moneda'
        verbose_name_plural = 'Monedas'

    def __str__(self):
        return f'{self.nombre}' 

class TipoComprobante(AuditModel):
    """ Clase para manejar tipos de comprobante  """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    es_credito = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tipo de Comprobante'
        verbose_name_plural = 'Tipos de Comprobante'

    def __str__(self):
        return f'{self.nombre}' 

class UnidadMedida(AuditModel):
    """ Clase para manejar unidades de medida  """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return f'{self.nombre}' 

class Idioma(AuditModel):
    """ Clase para manejar codigos de Idioma  """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idioma'

    def __str__(self):
        return f'{self.nombre}' 

class Incoterm(AuditModel):
    """ Clase para manejar incoterms """
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Incoterm'
        verbose_name_plural = 'Incoterms'

    def __str__(self):
        return f'{self.codigo}' 

class ConceptoIncluido(AuditModel):
    """ Clase para manejar los conceptos a facturar segun AFIP """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Concepto Incluido'
        verbose_name_plural = 'Conceptos Incluidos'

    def __str__(self):
        return f'{self.nombre}' 

class TipoResponsable(AuditModel):
    """ Clase para manejar los tipos de responsable """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)
    sigla = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Responsable'
        verbose_name_plural = 'Tipos de Responsable'

    def __str__(self):
        return f'{self.nombre}' 

class TipoSujeto(AuditModel):
    """ Clase para manejar los tipos de sujeto """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default='', unique=True)

    class Meta:
        verbose_name = 'Tipo de Sujeto'
        verbose_name_plural = 'Tipos de Sujeto'

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
        verbose_name_plural = 'Tipos de Documento'

    def __str__(self):
         return f'{self.nombre}'
    
class CuitPais(AuditModel):
    """ Tipos de documento de CUIT de los paises """
    
    idpais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    idtiposujeto = models.ForeignKey(TipoSujeto, on_delete=models.CASCADE)
    idmascara = models.ForeignKey(Mascara, on_delete=models.CASCADE)
    
    cuit = models.CharField(max_length=10, unique=True)

    class Meta:
        unique_together = (("idpais","idtiposujeto"),)
        verbose_name = 'CUIT Pais'
        verbose_name_plural = 'Paises CUIT'

    def __str__(self):
         return f'{self.idpais}, {self.idtiposujeto}, {self.cuit}'