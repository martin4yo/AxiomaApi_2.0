from rest_framework import serializers
from .funciones import producto_to_dict

from MasterModels.modelos_producto.producto import Producto
from MasterModels.modelos_producto.conversionproducto import ConversionProducto
from MasterModels.modelos_general.unidadmedida import UnidadMedida

from MasterSerializers.serializers_general import UnidadMedidaSerializer

class ConversionProductoSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idunidadmedida = serializers.PrimaryKeyRelatedField(
        queryset=UnidadMedida.objects.all(),
        write_only=True
    )
    idunidadmedida_detail = UnidadMedidaSerializer(source='idunidadmedida', read_only=True)

    idproducto = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        required=True,
        allow_null=True,
        write_only=True
    )
    idproducto_detail = serializers.SerializerMethodField()

    class Meta:
        """ Clase """
        model = ConversionProducto
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idprovincia': {'write_only': True},  # Asegura que se use en el POST
            'idpartido': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')
    
    def get_idproducto_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return producto_to_dict(obj.idproducto)

    # def get_idproducto_detail(self, obj):
    #     from MasterSerializers.serializers_producto.producto import ProductoSerializer
    #     return ProductoSerializer(obj.producto).data