from rest_framework import serializers
from .funciones import entidad_to_dict 

from MasterModels.modelos_entidad import Entidad, SectorEntidad
from MasterModels.modelos_general import Modulo, Sector
from MasterModels.modelos_impuestos import Impuesto

from MasterSerializers.serializers_general import ModuloSerializer, SectorSerializer

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

