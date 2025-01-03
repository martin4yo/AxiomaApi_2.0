from rest_framework import serializers
from .funciones import entidad_to_dict 

from MasterModels.modelos_entidad import Entidad, Zona, DireccionEntidad
from MasterModels.modelos_general import TipoSede, TipoDomicilio, Pais, Provincia, Partido, CodigoPostal

from MasterSerializers.serializers_general import TipoSedeSerializer, TipoDomicilioSerializer, PaisSerializer
from MasterSerializers.serializers_general import ProvinciaSerializer, PartidoSerializer, CodigoPostalSerializer
from MasterSerializers.serializers_entidad.zona import ZonaSerializer 

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

