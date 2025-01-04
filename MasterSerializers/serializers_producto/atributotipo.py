from rest_framework import serializers
from .funciones import producto_to_dict

from MasterModels.modelos_producto.atributo import Atributo
from MasterModels.modelos_producto.producto import Producto
from MasterModels.modelos_producto.atributoproducto import AtributoProducto
from MasterSerializers.serializers_producto.atributo import AtributoSerializer

class AtributoTipoSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idatributo = serializers.PrimaryKeyRelatedField(
        queryset=Atributo.objects.all(),
        write_only=True
    )
    idatributo_detail = AtributoSerializer(source='idatributo', read_only=True)

    idproducto = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        required=True,
        allow_null=True,
        write_only=True
    )
    idproducto_detail = serializers.SerializerMethodField()

    class Meta:
        """ Clase """
        model = AtributoProducto
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idatributo': {'write_only': True},  # Asegura que se use en el POST
            'idproducto': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    def get_idproducto_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return producto_to_dict(obj.idproducto)