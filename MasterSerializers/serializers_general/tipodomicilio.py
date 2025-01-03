from rest_framework import serializers
from MasterModels.modelos_general.tipodomicilio import TipoDomicilio

class TipoDomicilioSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoDomicilio
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

