from rest_framework import serializers
from MasterModels.modelos_general.tipofrecuencia import TipoFrecuencia


class TipoFrecuenciaSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoFrecuencia
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')