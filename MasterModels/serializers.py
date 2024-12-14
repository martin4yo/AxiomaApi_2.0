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

class FormaPagoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = FormaPago
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class FormaPagoDetalleSerializer(serializers.ModelSerializer):
    """ Serializador """

    idformapago = serializers.PrimaryKeyRelatedField(
        queryset=FormaPago.objects.all(),
        write_only=True
    )

    idformapago_detail = FormaPagoSerializer(source='idformapago', read_only=True)

    class Meta:
        """ Clase """
        model = FormaPagoDetalle
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idformapago': {'write_only': True},  # Asegura que se use en el POST
        }
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

    idpersona = serializers.PrimaryKeyRelatedField(
        queryset=Persona.objects.all(),
        write_only=True
    )
    idpersona_detail = PersonaSerializer(source='idpersona', read_only=True)

    idrol = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(),
        write_only=True
    )
    idrol_detail = RolSerializer(source='idrol', read_only=True)

    class Meta:
        """ Clase """
        model = PersonaRol
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idpersona': {'write_only': True},  # Asegura que se use en el POST
            'idrol': {'write_only': True},  # Asegura que se use en el POST
        }
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
    idpais = serializers.PrimaryKeyRelatedField(
        queryset=Pais.objects.all(),
        write_only=True
    )
    idpais_detail = PaisSerializer(source='idpais', read_only=True)

    class Meta:
        """ Clase """
        model = Provincia
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idpais': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class PartidoSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idprovincia = serializers.PrimaryKeyRelatedField(
        queryset=Provincia.objects.all(),
        write_only=True
    )
    idprovincia_detail = ProvinciaSerializer(source='idprovincia', read_only=True)


    class Meta:
        """ Clase """
        model = Partido
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idprovincia': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class CodigoPostalSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idprovincia = serializers.PrimaryKeyRelatedField(
        queryset=Provincia.objects.all(),
        write_only=True
    )
    idprovincia_detail = ProvinciaSerializer(source='idprovincia', read_only=True)

    idpartido = serializers.PrimaryKeyRelatedField(
        queryset=Partido.objects.all(),
        write_only=True
    )
    idpartido_detail = PartidoSerializer(source='idpartido', read_only=True)

    class Meta:
        """ Clase """
        model = CodigoPostal
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idprovincia': {'write_only': True},  # Asegura que se use en el POST
            'idpartido': {'write_only': True},  # Asegura que se use en el POST
        }
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

class TipoDeCambioSerializer(serializers.ModelSerializer):
    """ Serializador """

    idmoneda = serializers.PrimaryKeyRelatedField(
        queryset=Moneda.objects.all(),
        write_only=True
    )
    idmoneda_detail = MonedaSerializer(source='idmoneda', read_only=True)

    class Meta:
        """ Clase """
        model = TipoDeCambio
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmoneda': {'write_only': True},  # Asegura que `zona` se use en el POST
        }
        #fields = ['id', 'idmoneda','fecha','comprador']
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
 
    idmascara = serializers.PrimaryKeyRelatedField(
        queryset=Mascara.objects.all(),
        write_only=True
    )
    idmascara_detail = MascaraSerializer(source='idmascara', read_only=True)

    class Meta:
        """ Clase """
        model = TipoDocumento
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmascara': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class CuitPaisSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtiposujeto = serializers.PrimaryKeyRelatedField(
        queryset=TipoSujeto.objects.all(),
        write_only=True
    )

    idtiposujeto_detail = TipoSujetoSerializer(source='idtiposujeto', read_only=True)

    idmascara = serializers.PrimaryKeyRelatedField(
        queryset=Mascara.objects.all(),
        write_only=True
    )
    idmascara_detail = MascaraSerializer(source='idmascara', read_only=True)

    class Meta:
        """ Clase """
        model = CuitPais
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idtiposujeto': {'write_only': True},  # Asegura que se use en el POST
            'idmascara': {'write_only': True},  # Asegura que se use en el POST
        }
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

    idmoneda = serializers.PrimaryKeyRelatedField(
        queryset=Moneda.objects.all(),
        write_only=True
    )
    idmoneda_detail = MonedaSerializer(source='idmoneda', read_only=True)

    idtipofrecuencia = serializers.PrimaryKeyRelatedField(
        queryset=TipoFrecuencia.objects.all(),
        write_only=True
    )
    idtipofrecuencia_detail = TipoFrecuenciaSerializer(source='idtipofrecuencia', read_only=True)

    idtipovalor = serializers.PrimaryKeyRelatedField(
        queryset=TipoValor.objects.all(),
        write_only=True
    )
    idtipovalor_detail = TipoValorSerializer(source='idtipovalor', read_only=True)

    class Meta:
        """ Clase """
        model = TipoIndice
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmoneda': {'write_only': True},  # Asegura que se use en el POST
            'idtipofrecuencia': {'write_only': True},  # Asegura que se use en el POST
            'idtipovalor': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class IndiceSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtipoindice = serializers.PrimaryKeyRelatedField(
        queryset=TipoIndice.objects.all(),
        write_only=True
    )
    idtipoindice_detail = TipoIndiceSerializer(source='idtipoindice', read_only=True)

    class Meta:
        """ Clase """
        model = Indice
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idtipoindice': {'write_only': True},  # Asegura que se use en el POST
        }
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

    idclasificacionimpuesto = serializers.PrimaryKeyRelatedField(
        queryset=ClasificacionImpuesto.objects.all(),
        write_only=True
    )
    idclasificacionimpuesto_detail = ClasificacionImpuestoSerializer(source='idclasificacionimpuesto', read_only=True)

    class Meta:
        """ Clase """
        model = TipoImpuesto   
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idclasificacionimpuesto': {'write_only': True},  # Asegura que se use en el POST
        }
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

    idtipoimpuesto = serializers.PrimaryKeyRelatedField(
        queryset=TipoImpuesto.objects.all(),
        write_only=True
    )
    idtipoimpuesto_detail = TipoImpuestoSerializer(source='idclasificacionimpuesto', read_only=True)

    idalicuota = serializers.PrimaryKeyRelatedField(
        queryset=AlicuotaImpuesto.objects.all(),
        write_only=True
    )
    idalicuota_detail = AlicuotaImpuestoSerializer(source='idalicuota', read_only=True)

    idplancuenta = serializers.PrimaryKeyRelatedField(
        queryset=PlanCuentas.objects.all(),
        write_only=True
    )
    idplancuenta_detail = PlanCuentasSerializer(source='idplancuenta', read_only=True)

    idpadron = serializers.PrimaryKeyRelatedField(
        queryset=PadronImpuesto.objects.all(),
        write_only=True
    )
    idpadron_detail = PadronImpuestoSerializer(source='idpadron', read_only=True)

    idprovincia = serializers.PrimaryKeyRelatedField(
        queryset=Provincia.objects.all(),
        write_only=True
    )
    idprovincia_detail = ProvinciaSerializer(source='idprovincia', read_only=True)

    idpartido = serializers.PrimaryKeyRelatedField(
        queryset=Partido.objects.all(),
        write_only=True
    )
    idpartido_detail = PartidoSerializer(source='idpartido', read_only=True)

    class Meta:
        """ Clase """
        model = Impuesto   
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idimpuesto': {'write_only': True},  # Asegura que se use en el POST
            'idalicuota': {'write_only': True},  # Asegura que se use en el POST
            'idplancuenta': {'write_only': True},  # Asegura que se use en el POST
            'idpadron': {'write_only': True},  # Asegura que se use en el POST
            'idprovincia': {'write_only': True},  # Asegura que se use en el POST
            'idpartido': {'write_only': True},  # Asegura que se use en el POST
        }
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

from .models import Entidad, Zona, ListaPrecioEntidad, CondicionCrediticiaEntidad, ImpuestoEntidad, EjecutivoEntidad
from .models import DatosFiscalesEntidad, ContactoEntidad, TipoSede, TipoDomicilio, DireccionEntidad
from .models import ModuloEntidad, FormaPagoEntidad, SectorEntidad

class ModuloEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """

    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()

    idmodulo = serializers.PrimaryKeyRelatedField(
        queryset=Modulo.objects.all(),
        write_only=True
    )
    idmodulo_detail = ModuloSerializer(source='idmodulo', read_only=True)
    
    class Meta:
        """ Clase """
        model = ModuloEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'identidad': {'write_only': True},  # Asegura que se use en el POST
            'idmodulo': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

class DatosFiscalesEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()
    
    idtipodocumento = serializers.PrimaryKeyRelatedField(
        queryset=TipoDocumento.objects.all(),
        write_only=True
    )
    idtipodocumento_detail = TipoDocumentoSerializer(source='idtipodocumento', read_only=True)

    idtiposujeto = serializers.PrimaryKeyRelatedField(
        queryset=TipoSujeto.objects.all(),
        write_only=True
    )
    idtipodocumento_detail = TipoSujetoSerializer(source='idtiposujeto', read_only=True)

    class Meta:
        """ Clase """
        model = DatosFiscalesEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idtipodocumento': {'write_only': True},  # Asegura que se use en el POST
            'idtiposujeto': {'write_only': True},  # Asegura que se use en el POST
            'identidad': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

class EjecutivoEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """

    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()
    
    idpersona = serializers.PrimaryKeyRelatedField(
        queryset=Persona.objects.all(),
        write_only=True
    )
    idpersona_detail = PersonaSerializer(source='idpersona', read_only=True)

    idrol = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(),
        write_only=True
    )
    idrol_detail = RolSerializer(source='idrol', read_only=True)

    class Meta:
        """ Clase """
        model = EjecutivoEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idpersona': {'write_only': True},  # Asegura que se use en el POST
            'idrol': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')
    
    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

class ZonaSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = Zona
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class FormaPagoEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """

    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()

    idmodulo = serializers.PrimaryKeyRelatedField(
        queryset=Modulo.objects.all(),
        write_only=True
    )
    idmodulo_detail = ModuloSerializer(source='idmodulo', read_only=True)

    idformapago = serializers.PrimaryKeyRelatedField(
        queryset=FormaPago.objects.all(),
        write_only=True
    )
    idformapago_detail = FormaPagoSerializer(source='idformapago', read_only=True)
    
    class Meta:
        """ Clase """
        model = FormaPagoEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'identidad': {'write_only': True},  # Asegura que se use en el POST
            'idmodulo': {'write_only': True},  # Asegura que se use en el POST
            'idformapago': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

class SectorEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()

    idmodulo = serializers.PrimaryKeyRelatedField(
        queryset=Modulo.objects.all(),
        write_only=True
    )
    idmodulo_detail = ModuloSerializer(source='idmodulo', read_only=True)

    idsector = serializers.PrimaryKeyRelatedField(
        queryset=Sector.objects.all(),
        write_only=True
    )
    idsector_detail = SectorSerializer(source='idsector', read_only=True)

    class Meta:
        """ Clase """
        model = SectorEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'identidad': {'write_only': True},  # Asegura que se use en el POST
            'idmodulo': {'write_only': True},  # Asegura que se use en el POST
            'idsector': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

class ContactoEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()

    class Meta:
        """ Clase """
        model = ContactoEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'identidad': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

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

    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()
    
    idmodulo = serializers.PrimaryKeyRelatedField(
        queryset=Modulo.objects.all(),
        write_only=True
    )
    idmodulo_detail = ModuloSerializer(source='idmodulo', read_only=True)

    idlistaprecio = serializers.PrimaryKeyRelatedField(
        queryset=ListaPrecios.objects.all(),
        write_only=True
    )
    idlistaprecio_detail = ListaPreciosSerializer(source='idlistaprecio', read_only=True)

    class Meta:
        """ Clase """
        model = ListaPrecioEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmodulo': {'write_only': True},  # Asegura que se use en el POST
            'idlistaprecio': {'write_only': True},  # Asegura que se use en el POST
            'identidad': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

class CondicionCrediticiaEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """

    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()
    
    idmodulo = serializers.PrimaryKeyRelatedField(
        queryset=Modulo.objects.all(),
        write_only=True
    )
    idmodulo_detail = ModuloSerializer(source='idmodulo', read_only=True)

    class Meta:
        """ Clase """
        model = CondicionCrediticiaEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmodulo': {'write_only': True},  # Asegura que se use en el POST
            'identidad': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')
        depth = 1

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

class ImpuestoEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """

    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()
    
    idmodulo = serializers.PrimaryKeyRelatedField(
        queryset=Modulo.objects.all(),
        write_only=True
    )
    idmodulo_detail = ModuloSerializer(source='idmodulo', read_only=True)

    idimpuesto = serializers.PrimaryKeyRelatedField(
        queryset=Impuesto.objects.all(),
        write_only=True
    )
    idimpuesto_detail = ImpuestoSerializer(source='idimpuesto', read_only=True)

    class Meta:
        """ Clase """
        model = ImpuestoEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmodulo': {'write_only': True},  # Asegura que se use en el POST
            'idimpuesto': {'write_only': True},  # Asegura que se use en el POST
            'identidad': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

class DireccionEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """

    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()
    
    idtiposede = serializers.PrimaryKeyRelatedField(
        queryset=TipoSede.objects.all(),
        write_only=True
    )
    idtiposede_detail = TipoSedeSerializer(source='idtiposede', read_only=True)

    idtipodomicilio = serializers.PrimaryKeyRelatedField(
        queryset=TipoDomicilio.objects.all(),
        write_only=True
    )
    idtipodomicilio_detail = TipoDomicilioSerializer(source='idtipodomicilio', read_only=True)

    idpais = serializers.PrimaryKeyRelatedField(
        queryset=Pais.objects.all(),
        write_only=True
    )
    idpais_detail = PaisSerializer(source='idpais', read_only=True)

    idprovincia = serializers.PrimaryKeyRelatedField(
        queryset=Provincia.objects.all(),
        write_only=True
    )
    idprovincia_detail = ProvinciaSerializer(source='idprovincia', read_only=True)

    idpartido = serializers.PrimaryKeyRelatedField(
        queryset=Partido.objects.all(),
        write_only=True
    )
    idpartido_detail = PartidoSerializer(source='idpartido', read_only=True)

    idcodigopostal = serializers.PrimaryKeyRelatedField(
        queryset=CodigoPostal.objects.all(),
        write_only=True
    )
    idcodigopostal_detail = CodigoPostalSerializer(source='idcodigopostal', read_only=True)

    idzona = serializers.PrimaryKeyRelatedField(
        queryset=Zona.objects.all(),
        write_only=True
    )
    idzona_detail = ZonaSerializer(source='idzona', read_only=True)

    class Meta:
        """ Clase """
        model = DireccionEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'identidad': {'write_only': True},  # Asegura que se use en el POST
            'idtiposede': {'write_only': True},  # Asegura que se use en el POST
            'idtipodomicilio': {'write_only': True},  # Asegura que se use en el POST
            'idpais': {'write_only': True},  # Asegura que se use en el POST
            'idprovincia': {'write_only': True},  # Asegura que se use en el POST
            'idpartido': {'write_only': True},  # Asegura que se use en el POST
            'idcodigopostal': {'write_only': True},  # Asegura que se use en el POST
            'idzona': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

class EntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    entidad_moduloentidad = ModuloEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    entidad_condicionecrediticia = CondicionCrediticiaEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    entidad_impuestoentidad = ImpuestoEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    entidad_ejecutivo = EjecutivoEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    entidad_datosfiscalesentidad = DatosFiscalesEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    entidad_contacto = ContactoEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    entidad_direcciones = DireccionEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    entidad_sectorentidad = SectorEntidadSerializer(many=True, read_only=True)  # Anidar el serializador
    entidad_formapagoentidad = FormaPagoEntidadSerializer(many=True, read_only=True)

    idtiporesponsable = serializers.PrimaryKeyRelatedField(
        queryset=TipoResponsable.objects.all(),
        write_only=True
    )
    idtiporesponsable_detail = TipoResponsableSerializer(source='idtiporesponsable', read_only=True)

    class Meta:
        """ Clase """
        model = Entidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idtiporesponsable': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_entidad_moduloentidad(self, obj):
        """ Serializa los módulos asociados a la entidad """
        modulos = ModuloEntidad.objects.filter(identidad=obj)
        return ModuloEntidadSerializer(modulos, many=True).data
    
# Funcion para devolver la lista de campos de Entidad

def entidad_to_dict(entidad):
    """
    Convierte una instancia de Entidad en un diccionario.
    """
    return {
        'id': entidad.id,
        'nombre': entidad.nombre,  # Ajusta según los campos que tengas en Entidad
        'nombrefantasia': entidad.nombrefantasia,  # Ajusta según los campos que tengas en Entidad
        'codigo': entidad.codigo,  # Ajusta según los campos que tengas en Entidad
        'intercompany': entidad.intercompany,  # Ajusta según los campos que tengas en Entidad
        
    }