"""
Serializadores
"""
from rest_framework import serializers
from .models import Persona, PersonaRol, Pais, Provincia, CodigoPostal, TipoDeCambio
from .models import Rol, Modulo, Mascara, FormaDePago, FormaDePagoDetalle, Moneda
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

    idformadepago = Moneda

    class Meta:
        """ Clase """
        model = TipoDeCambio
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class FormaDePagoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = FormaDePago
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class FormaDePagoDetalleSerializer(serializers.ModelSerializer):
    """ Serializador """

    idformadepago = FormaDePagoSerializer

    class Meta:
        """ Clase """
        model = FormaDePagoDetalle
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

class CodigoPostalSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idprovincia = ProvinciaSerializer()

    class Meta:
        """ Clase """
        model = CodigoPostal
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

### IMPOSITIVO ###############################################################

from .models import TipoDocumento, TipoSujeto, TipoResponsable, ConceptoIncluido, Incoterm
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

class IncotermSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Incoterm   
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
    
    idpais = PaisSerializer()
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

from .models import TipoAjuste, PlanDeCuentas

class TipoaAjusteSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoAjuste
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PlanDeCuentasSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = PlanDeCuentas
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


## IMPUESTOS QUE TIENEN FK A MODULOS ANTERIORES ##################################

class ImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """

    idtipoimpuesto = TipoImpuestoSerializer()
    idalicuota = AlicuotaImpuestoSerializer()
    idplandecuenta = PlanDeCuentasSerializer()
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

from .models import Entidad, Zona, ListaPrecioEntidad, CondicionCrediticia

class EntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtiporesponsable = TipoResponsableSerializer()

    class Meta:
        """ Clase """
        model = Entidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ZonaSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = Zona
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ListaPrecioEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    identidad = EntidadSerializer()
    idmodulo = ModuloSerializer()
    idlistaprecio = ListaPreciosSerializer()

    class Meta:
        """ Clase """
        model = ListaPrecioEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class CondicionCrediticiaSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    identidad = EntidadSerializer()
    idmodulo = ModuloSerializer()

    class Meta:
        """ Clase """
        model = CondicionCrediticia
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')
