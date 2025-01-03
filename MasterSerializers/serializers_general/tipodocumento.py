from rest_framework import serializers
from MasterModels.modelos_general.tipodocumento import TipoDocumento
from MasterModels.modelos_general.mascara import Mascara

from MasterSerializers.serializers_general.mascara import MascaraSerializer


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


