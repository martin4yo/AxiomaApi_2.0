from django.db import models
from .universal import AuditModel, TenantModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

# Generales ########################################################################

class TipoDeCambio(AuditModel, TenantModel):
    """ Clase para manejar los roles """
    fecha = models.DateField()
    idmoneda = models.ForeignKey('Moneda', on_delete=models.CASCADE, related_name='moneda_tipocambio')
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
    idformapago = models.ForeignKey('FormaPago', on_delete=models.CASCADE, related_name='formapago_detalle')

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
    idpartido = models.ForeignKey('Partido', on_delete=models.CASCADE, related_name='partido_codigopostal')

    class Meta:
        verbose_name = 'Codigo Postal'
        verbose_name_plural = 'GRAL - Codigos Postales'

    def __str__(self):
        return f'{self.nombre}'
    
class Partido(AuditModel):
    """ Clase para manejar los datos de partidos """
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    idprovincia = models.ForeignKey('Provincia', on_delete=models.CASCADE, related_name='provincia_partido')
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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
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
    idtipoindice = models.ForeignKey('TipoIndice', on_delete=models.CASCADE, related_name='tipoindice_indice')
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
    idmascara = models.ForeignKey(Mascara, on_delete=models.CASCADE, related_name='mascara_tipodocumento')
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
    idmoneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name='moneda_tipoindice')
    idtipofrecuencia = models.ForeignKey('TipoFrecuencia', on_delete=models.CASCADE, related_name='tipofrecuencia_tipoindice')
    idtipovalor = models.ForeignKey('TipoValor', on_delete=models.CASCADE, related_name='tipovalor_tipoindice')
                                    
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