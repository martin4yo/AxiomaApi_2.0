from rest_framework import serializers
from MasterModels.modelos_general.partido import Partido
from MasterModels.modelos_general.provincia import Provincia
from .provincia import ProvinciaSerializer

class PartidoSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idprovincia = serializers.PrimaryKeyRelatedField(
        queryset=Provincia.objects.all(),
        write_only=True
    )
    idprovincia_detail = ProvinciaSerializer(source='idprovincia', read_only=True)

    class Meta:
        """ Clase """
        model = Partido
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idprovincia': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

