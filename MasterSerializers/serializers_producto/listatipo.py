from rest_framework import serializers
from MasterModels.modelos_producto.listatipo import ListaTipo

class ListaTipoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = ListaTipo
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')
