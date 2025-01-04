from rest_framework import serializers
from .funciones import producto_to_dict

from MasterModels.modelos_producto.producto import Producto
from MasterModels.modelos_producto.contabilidadproducto import ContabilidadProducto
from MasterModels.modelos_contabilidad.plancuenta import PlanCuenta

from MasterSerializers.serializers_contabilidad.plancuenta import PlanCuentaSerializer

class ContabilidadProductoSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idplancuenta = serializers.PrimaryKeyRelatedField(
        queryset=PlanCuenta.objects.all(),
        write_only=True
    )
    idplancuenta_detail = PlanCuentaSerializer(source='idplancuenta', read_only=True)

    idproducto = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        required=True,
        allow_null=True,
        write_only=True
    )
    idproducto_detail = serializers.SerializerMethodField()

    class Meta:
        """ Clase """
        model = ContabilidadProducto
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