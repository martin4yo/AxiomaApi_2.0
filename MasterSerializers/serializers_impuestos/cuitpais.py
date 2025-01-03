from rest_framework import serializers
from MasterModels.modelos_impuestos import CuitPais, TipoSujeto
from MasterModels.modelos_general import Pais, TipoDocumento

from MasterSerializers.serializers_general import TipoDocumentoSerializer, PaisSerializer
from MasterSerializers.serializers_impuestos.tiposujeto import TipoSujetoSerializer

class CuitPaisSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtiposujeto = serializers.PrimaryKeyRelatedField(
        queryset=TipoSujeto.objects.all(),
        write_only=True
    )

    idtiposujeto_detail = TipoSujetoSerializer(source='idtiposujeto', read_only=True)

    idpais = serializers.PrimaryKeyRelatedField(
        queryset=Pais.objects.all(),
        write_only=True
    )
    idpais_detail = PaisSerializer(source='idpais', read_only=True)

    idtipodocumento = serializers.PrimaryKeyRelatedField(
        queryset=TipoDocumento.objects.all(),
        write_only=True
    )
    idtipodocumento_detail = TipoDocumentoSerializer(source='idtipodocumento', read_only=True)


    class Meta:
        """ Clase """
        model = CuitPais
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idtiposujeto': {'write_only': True},  # Asegura que se use en el POST
            'idmascara': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')