from rest_framework import serializers

from MasterModels.modelos_producto.listatipo import ListaTipo
from MasterModels.modelos_producto.listaprecio import ListaPrecio

from MasterSerializers.serializers_producto.listatipo import ListaTipoSerializer

class ListaPrecioSerializer(serializers.ModelSerializer):
    
    """ Serializadores """
    idtipolista = serializers.PrimaryKeyRelatedField(
        queryset=ListaTipo.objects.all(),
        write_only=True
    )
    idtipolista_detail = ListaTipoSerializer(source='idtipolista', read_only=True)
    
    class Meta:
        """ Clase """
        model = ListaPrecio
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')