"""
Serializadores
"""
from rest_framework import serializers
from .models import Persona, PersonaRol, Pais, Provincia, CodigoPostal, TipoDeCambio
from .models import Rol, Modulo, Mascara, FormaPago, FormaPagoDetalle, Moneda
from .models import Partido, Sector

### Generales ######################################################

class SectorSerializer(serializers.ModelSerializer):
    """ Serializador """

    class Meta:
        """ Clase """
        model = Sector
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoDeCambioSerializer(serializers.ModelSerializer):
    """ Serializador """

    idmoneda = Moneda

    class Meta:
        """ Clase """
        model = TipoDeCambio
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class FormaPagoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = FormaPago
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class FormaPagoDetalleSerializer(serializers.ModelSerializer):
    """ Serializador """

    idformapago = FormaPagoSerializer

    class Meta:
        """ Clase """
        model = FormaPagoDetalle
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class MascaraSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Mascara
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ModuloSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Modulo
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class RolSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Rol
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PersonaSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Persona
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PersonaRolSerializer(serializers.ModelSerializer):
    """ Serializador """

    idpersona = PersonaSerializer()
    idrol = RolSerializer()

    class Meta:
        """ Clase """
        model = PersonaRol
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PaisSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Pais
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ProvinciaSerializer(serializers.ModelSerializer):
    """ Serializador """
    idpais = PaisSerializer()

    class Meta:
        """ Clase """
        model = Provincia
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PartidoSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idprovincia = ProvinciaSerializer()

    class Meta:
        """ Clase """
        model = Partido
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class CodigoPostalSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idprovincia = ProvinciaSerializer()
    idpartido = PartidoSerializer()
    class Meta:
        """ Clase """
        model = CodigoPostal
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

### IMPOSITIVO ###############################################################

from .models import TipoDocumento, TipoSujeto, TipoResponsable, ConceptoIncluido, Incoterms
from .models import Idioma, UnidadMedida, TipoComprobante, CuitPais, TipoIndice, AlicuotaImpuesto
from .models import PadronImpuesto, TipoFrecuencia, TipoValor, TipoCalculo, Indice, ClasificacionImpuesto
from .models import TipoImpuesto, Impuesto

class TipoCalculoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = TipoCalculo   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class MonedaSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Moneda   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoComprobanteSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = TipoComprobante   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class UnidadMedidaSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = UnidadMedida   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class IdiomaSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Idioma   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class IncotermsSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Incoterms   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ConceptoIncluidoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = ConceptoIncluido
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoResponsableSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = TipoResponsable
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoSujetoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = TipoSujeto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoDocumentoSerializer(serializers.ModelSerializer):
    """ Serializador """
 
    idmascara = MascaraSerializer()

    class Meta:
        """ Clase """
        model = TipoDocumento
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class CuitPaisSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtiposujeto = TipoSujetoSerializer()
    idmascara = MascaraSerializer()

    class Meta:
        """ Clase """
        model = CuitPais
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoFrecuenciaSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoFrecuencia
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


class TipoValorSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoValor
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


class TipoIndiceSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idmoneda = MonedaSerializer()
    idtipofrecuencia = TipoFrecuenciaSerializer()
    idtipovalor = TipoValorSerializer()

    class Meta:
        """ Clase """
        model = TipoIndice
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class IndiceSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtipoindice = TipoIndiceSerializer()

    class Meta:
        """ Clase """
        model = Indice
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class AlicuotaImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = AlicuotaImpuesto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PadronImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = PadronImpuesto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ClasificacionImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = ClasificacionImpuesto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """

    idclasificacionimpuesto = ClasificacionImpuestoSerializer()

    class Meta:
        """ Clase """
        model = TipoImpuesto   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

### CONTABLE ###############################################################

from .models import TipoAjuste, PlanCuentas

class TipoaAjusteSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoAjuste
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PlanCuentasSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = PlanCuentas
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


## IMPUESTOS QUE TIENEN FK A MODULOS ANTERIORES ##################################

class ImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """

    idtipoimpuesto = TipoImpuestoSerializer()
    idalicuota = AlicuotaImpuestoSerializer()
    idplancuenta = PlanCuentasSerializer()
    idpadron = PadronImpuestoSerializer()
    idprovincia = ProvinciaSerializer()
    idpartido = PartidoSerializer()

    class Meta:
        """ Clase """
        model = Impuesto   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


## PRODUCTOS ##################################

from .models import ListaPrecios

class ListaPreciosSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = ListaPrecios
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

## ENTIDADES ##################################

from .models import Entidad, Zona, ListaPrecioEntidad, CondicionCrediticia, ImpuestoEntidad, Ejecutivo
from .models import DatosFiscalesEntidad, ContactoEntidad, TipoSede, TipoDomicilio, DireccionEntidad
from .models import ModuloEntidad, FormaPagoEntidad, SectorEntidad

class ModuloEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = ModuloEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class DatosFiscalesEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtipodocumento = TipoDocumentoSerializer()
    idtiposujeto = TipoSujetoSerializer()

    class Meta:
        """ Clase """
        model = DatosFiscalesEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class EjecutivoSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idpersona = PersonaSerializer()
    idrol = RolSerializer()

    class Meta:
        """ Clase """
        model = Ejecutivo
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ZonaSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = Zona
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class FormaPagoEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = FormaPagoEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class SectorEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = SectorEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ContactoEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = ContactoEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoSedeSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoSede
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoDomicilioSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoDomicilio
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ListaPrecioEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idmodulo = ModuloSerializer()
    idlistaprecio = ListaPreciosSerializer()

    class Meta:
        """ Clase """
        model = ListaPrecioEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class CondicionCrediticiaSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idmodulo = ModuloSerializer()

    class Meta:
        """ Clase """
        model = CondicionCrediticia
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ImpuestoEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idmodulo = ModuloSerializer()
    idimpuesto = ImpuestoSerializer()

    class Meta:
        """ Clase """
        model = ImpuestoEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class DireccionEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtiposede = TipoSedeSerializer()
    idtipodomicilio = TipoDomicilioSerializer()
    idpais = PaisSerializer()
    idprovincia = ProvinciaSerializer()
    idpartido = PartidoSerializer()
    idcodigopostal = CodigoPostalSerializer()
    idzona = ZonaSerializer()

    class Meta:
        """ Clase """
        model = DireccionEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class EntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    modulos = ModuloEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    condicionescrediticias = CondicionCrediticiaSerializer(many=True, read_only=True)  # Anidar el serializador
    impuestos = ImpuestoEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    ejecutivos = EjecutivoSerializer(many=True, read_only=True)  # Anidar el serializador
    datosfiscales = DatosFiscalesEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    contactos = ContactoEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    direcciones = DireccionEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    sectores = SectorEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    formaspago = FormaPagoSerializer(many=True, read_only=True)

    idtiporesponsable = TipoResponsableSerializer()

    class Meta:
        """ Clase """
        model = Entidad
        fields = ['id', 'nombre', 'nombrefantasia', 'idtiporesponsable', 'modulos', 'condicionescrediticias',
                  'impuestos','ejecutivos','datosfiscales','contactos','direcciones','sectores','formaspago']  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')