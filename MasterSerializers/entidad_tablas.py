from rest_framework import serializers

## ENTIDADES ##################################

from MasterModels.general import TipoSede, TipoDomicilio, Modulo, TipoDocumento, Persona, Rol, FormaPago, Sector
from MasterModels.general import Partido, Provincia, CodigoPostal, Pais
from MasterModels.impuestos import TipoSujeto, Impuesto
from MasterModels.producto import ListaPrecioEntidad, ListaPrecios
from MasterModels.entidad import Entidad, Zona, CondicionCrediticiaEntidad, ImpuestoEntidad, EjecutivoEntidad
from MasterModels.entidad import DatosFiscalesEntidad, ContactoEntidad, DireccionEntidad
from MasterModels.entidad import ModuloEntidad, FormaPagoEntidad, SectorEntidad

from MasterSerializers.general import ModuloSerializer, PersonaSerializer, RolSerializer, FormaPagoSerializer, SectorSerializer
from MasterSerializers.general import PartidoSerializer, ProvinciaSerializer, CodigoPostalSerializer, PaisSerializer
from MasterSerializers.impuestos import TipoDocumentoSerializer, TipoSujetoSerializer, ImpuestoSerializer
from MasterSerializers.producto import ListaPreciosSerializer

class ModuloEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """

    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        required=False,
        allow_null=True,
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
            'identidad': {'write_only': True, 'required': False},  # Asegura que se use en el POST
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
        required=False,
        allow_null=True,
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
    idtiposujeto_detail = TipoSujetoSerializer(source='idtiposujeto', read_only=True)

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
        required=False,
        allow_null=True,
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
        required=False,
        allow_null=True,
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
        required=False,
        allow_null=True,
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
        required=False,
        allow_null=True,
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
        required=False,
        allow_null=True,
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
        required=False,
        allow_null=True,
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
        required=False,
        allow_null=True,
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