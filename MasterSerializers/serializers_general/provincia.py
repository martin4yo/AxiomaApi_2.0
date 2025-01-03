from rest_framework import serializers
from MasterModels.modelos_general.pais import Pais
from MasterModels.modelos_general.provincia import Provincia

from .pais import PaisSerializer

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
