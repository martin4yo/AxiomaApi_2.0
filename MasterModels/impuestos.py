from django.db import models
from .universal import AuditModel

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
    
    idtiposujeto = models.ForeignKey(TipoSujeto, on_delete=models.CASCADE, related_name='tiposujeto_cuitpais')
    nombre = models.CharField(max_length=256, default='')
    idmascara = models.ForeignKey('Mascara', on_delete=models.CASCADE, related_name='mascara_cuitpais')
    idpais = models.ForeignKey('Pais', on_delete=models.CASCADE, related_name='pais_cuitpais')
    
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
    idclasificacionimpuesto = models.ForeignKey(ClasificacionImpuesto, on_delete=models.CASCADE, related_name='clasificacionimpuesto_tipoimpuesto')
    
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
    idtipoimpuesto = models.ForeignKey(TipoImpuesto, on_delete=models.CASCADE, related_name='tipoimpuesto_impuesto')
    idalicuota = models.ForeignKey(AlicuotaImpuesto, on_delete=models.CASCADE, related_name='alicuota_impuesto')
    idpadron = models.ForeignKey(PadronImpuesto, on_delete=models.CASCADE, blank=True, null=True, related_name='padron_impuesto')
    idprovincia = models.ForeignKey('Provincia', on_delete=models.CASCADE, blank=True, null=True, related_name='provincia_impuesto')
    idpartido = models.ForeignKey('Partido', on_delete=models.CASCADE, blank=True, null=True, related_name='partido_impuesto')
    
    class Meta:
        unique_together = (("codigo"),)
        verbose_name = 'Impuesto'
        verbose_name_plural = 'IMPU - Impuestos'

    def __str__(self):
         return f'{self.nombre}, {self.codigo}, {self.idtipoimpuesto}'