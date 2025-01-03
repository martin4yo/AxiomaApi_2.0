from rest_framework import serializers
from MasterModels.modelos_general.codigopostal import CodigoPostal
from MasterModels.modelos_general.provincia import Provincia
from MasterModels.modelos_general.partido import Partido
from .provincia import ProvinciaSerializer
from .partido import PartidoSerializer

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