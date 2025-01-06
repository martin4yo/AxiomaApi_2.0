from rest_framework import serializers
from MasterModels.modelos_general.modulo import Modulo

class ModuloSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Modulo
        #fields = '__all__'  # O especifica los campos que deseas incluir
        fields = ['id','codigo','nombre']
        read_only_fields = ('created_at', 'updated_at')


