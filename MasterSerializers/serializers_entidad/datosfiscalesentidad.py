from rest_framework import serializers
from .funciones import entidad_to_dict 

from MasterModels.modelos_entidad import Entidad, DatosFiscalesEntidad
from MasterModels.modelos_general.tipodocumento import TipoDocumento
from MasterModels.modelos_impuestos.tiposujeto import TipoSujeto

from MasterSerializers.serializers_general import TipoDocumentoSerializer
from MasterSerializers.serializers_impuestos.tiposujeto import TipoSujetoSerializer


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

