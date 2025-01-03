from rest_framework import serializers
from MasterModels.modelos_general import Indice, TipoIndice

from MasterSerializers.serializers_general.tipoindice import TipoIndiceSerializer

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