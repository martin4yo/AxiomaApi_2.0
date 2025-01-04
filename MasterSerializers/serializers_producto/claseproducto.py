from rest_framework import serializers
from MasterModels.modelos_producto.claseproducto import ClaseProducto

class ClaseProductoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = ClaseProducto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


