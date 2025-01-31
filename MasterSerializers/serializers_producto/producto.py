from rest_framework import serializers
from django.db import transaction
from .funciones import insert_tabla_asociada

from MasterSerializers.serializers_producto.atributoproducto import AtributoProductoSerializer
from MasterSerializers.serializers_producto.contabilidadproducto import ContabilidadProductoSerializer
from MasterSerializers.serializers_producto.conversionproducto import ConversionProductoSerializer
from MasterSerializers.serializers_producto.precio import PrecioSerializer

from MasterSerializers.serializers_producto.tipoproducto import TipoProductoSerializer
from MasterSerializers.serializers_general.unidadmedida import UnidadMedidaSerializer
from MasterSerializers.serializers_producto.claseproducto import ClaseProductoSerializer

from MasterModels.modelos_producto import TipoProducto, Producto, ClaseProducto, AtributoProducto, ContabilidadProducto, ConversionProducto
from MasterModels.modelos_producto import Precio
from MasterModels.modelos_general import UnidadMedida

class ProductoSerializer(serializers.ModelSerializer):
    """ Serializador """
   
    producto_atributo = AtributoProductoSerializer(many=True, required=False)  # Anidar el serializador
    producto_contabilidad = ContabilidadProductoSerializer(many=True, required=False)  # Anidar el serializador
    producto_conversion = ConversionProductoSerializer(many=True, required=False)  # Anidar el serializador
    producto_precio = PrecioSerializer(many=True, required=False)  # Anidar el serializador

    idtipoproducto = serializers.PrimaryKeyRelatedField(
        queryset=TipoProducto.objects.all(),
        required=False,
        allow_null=True,
        write_only=True
    )
    idtipoproducto_detail = TipoProductoSerializer(source='idtipoproducto', read_only=True, required=False)

    idunidadmedida = serializers.PrimaryKeyRelatedField(
        queryset=UnidadMedida.objects.all(),
        required=False,
        allow_null=True,
        write_only=True
    )
    idunidadmedida_detail = UnidadMedidaSerializer(source='idunidadmedida', read_only=True, required=False)

    idclaseproducto = serializers.PrimaryKeyRelatedField(
        queryset=ClaseProducto.objects.all(),
        required=False,
        allow_null=True,
        write_only=True
    )
    idclaseproducto_detail = ClaseProductoSerializer(source='idclaseproducto', read_only=True, required=False)

    class Meta:
        """ Clase """
        model = Producto
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idtipoproducto': {'write_only': True},  # Asegura que se use en el POST
            'idunidadmedida': {'write_only': True},  # Asegura que se use en el POST
            'idclaseproducto': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')
        
    def create(self, validated_data):
        try:

            producto_atributo = validated_data.pop('producto_atributo', [])
            producto_contabilidad = validated_data.pop('producto_contabilidad', [])
            producto_conversion = validated_data.pop('producto_conversion', [])
            producto_precio = validated_data.pop('producto_precio', [])         
            
            with transaction.atomic():

                producto = Producto.objects.create(**validated_data)

                insert_tabla_asociada(self, producto, AtributoProducto, producto_atributo)
                insert_tabla_asociada(self, producto, ContabilidadProducto, producto_contabilidad)
                insert_tabla_asociada(self, producto, ConversionProducto, producto_conversion)
                insert_tabla_asociada(self, producto, Precio, producto_precio)

            return producto
        
        except serializers.ValidationError as e:
            print(f"Validation errors: {e}")
            raise

    # Update del producto
    
    def update(self, instance, validated_data):

        instance.idtipoproducto = validated_data.get('idtipoproducto', instance.idtipoproducto)
        instance.codigo = validated_data.get('codigo', instance.codigo)
        instance.nombre = validated_data.get('codigo', instance.codigo)
        instance.modificatexto = validated_data.get('modificatexto', instance.modificatexto)
        instance.ean = validated_data.get('ean', instance.ean)
        instance.idunidadmedida = validated_data.get('idunidadmedida', instance.idunidadmedida)
        instance.idclaseproducto = validated_data.get('idclaseproducto', instance.idclaseproducto)
        instance.decimales = validated_data.get('decimales', instance.decimales)
        instance.stockminimo = validated_data.get('stockminimo', instance.stockminimo)
        instance.stockmaximo = validated_data.get('stockmaximo', instance.stockmaximo)
        instance.puntopedido = validated_data.get('puntopedido', instance.puntopedido)
        instance.avisapedido = validated_data.get('avisapedido', instance.avisapedido)
        instance.avisaminimo = validated_data.get('avisaminimo', instance.avisaminimo)
        instance.precicostopromedio = validated_data.get('precicostopromedio', instance.precicostopromedio)
        instance.precioreferencia = validated_data.get('precioreferencia', instance.precioreferencia)
        instance.precioultimacompra = validated_data.get('precioultimacompra', instance.precioultimacompra)
        instance.preciocostostandard = validated_data.get('preciocostostandard', instance.preciocostostandard)
        
        instance.save()

        # Actualizar tablas asociadas ############################################################################################

        if 'producto_atributo' in validated_data:
            insert_tabla_asociada(self, instance, AtributoProducto, validated_data.pop('producto_atributo', []))

        if 'producto_contabilidad' in validated_data:
            insert_tabla_asociada(self, instance, ContabilidadProducto, validated_data.pop('producto_contabilidad', []))

        if 'producto_conversion' in validated_data:
            insert_tabla_asociada(self, instance, ConversionProducto, validated_data.pop('producto_conversion', []))

        if 'producto_precio' in validated_data:
            insert_tabla_asociada(self, instance, Precio, validated_data.pop('producto_precio', []))

        return instance    
    
    # def validate(self, attrs):
    #     request = self.context.get('request')  # Obtenemos el tipo de solicitud
    #     if request and request.method == 'POST':
    #         # En POST, aseguramos que 'nombre' esté presente y no sea vacío
    #         if 'codigo' not in attrs or not attrs['codigo'].strip():
    #             raise serializers.ValidationError({
    #                 'codigo': 'Este campo es obligatorio para crear una entidad.'
    #             })
    #         # En POST, aseguramos que 'nombre' esté presente y no sea vacío
    #         if 'idtiporesponsable' not in attrs or not attrs['idtiporesponsable'].strip():
    #             raise serializers.ValidationError({
    #                 'idtiporesponsable': 'Este campo es obligatorio para crear una entidad.'
    #             })
    #     return attrs
    
