from rest_framework import serializers
from .funciones import entidad_to_dict

from MasterModels.modelos_entidad import Entidad, ImpuestoEntidad
from MasterModels.modelos_general import Modulo
from MasterModels.modelos_impuestos import Impuesto

from MasterSerializers.serializers_general import ModuloSerializer
from MasterSerializers.serializers_impuestos import ImpuestoSerializer


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
        # extra_kwargs = {
        #     'idmodulo': {'write_only': True},  # Asegura que se use en el POST
        #     'idimpuesto': {'write_only': True},  # Asegura que se use en el POST
        #     'identidad': {'write_only': True},  # Asegura que se use en el POST
        # }
        read_only_fields = ('created_at', 'updated_at')

    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

