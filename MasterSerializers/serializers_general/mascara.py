from rest_framework import serializers
from MasterModels.modelos_general.mascara import Mascara

class MascaraSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Mascara
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


