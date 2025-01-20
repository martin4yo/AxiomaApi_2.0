from rest_framework import serializers
from .funciones import producto_to_dict

from MasterModels.modelos_producto.precio import Precio
from MasterModels.modelos_producto.listaprecio import ListaPrecio
from MasterModels.modelos_producto.producto import Producto

from MasterSerializers.serializers_producto import ListaPrecioSerializer

class PrecioSerializer(serializers.ModelSerializer):

    idlistaprecio = serializers.PrimaryKeyRelatedField(
        queryset=ListaPrecio.objects.all(),
        write_only=True
    )
    idlistaprecio_detail = ListaPrecioSerializer(source='idlistaprecio', read_only=True)

    idproducto = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        required=True,
        allow_null=True,
        write_only=True
    )
    idproducto_detail = serializers.SerializerMethodField()

    """ Serializador """
    class Meta:
        """ Clase """
        model = Precio
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

    def get_idproducto_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return producto_to_dict(obj.idproducto)