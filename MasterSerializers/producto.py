from rest_framework import serializers

## PRODUCTOS ##################################

from MasterModels.producto import ListaPrecios

class ListaPreciosSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = ListaPrecios
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

