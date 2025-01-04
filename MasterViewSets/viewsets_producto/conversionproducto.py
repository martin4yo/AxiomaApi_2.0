from MasterViewSets.universal import *

from MasterModels.modelos_producto import ConversionProducto

from MasterSerializers.serializers_producto import ConversionProductoSerializer

class ConversionProductoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = ConversionProducto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ConversionProductoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ConversionProducto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ConversionProducto
    
    filterset_class = FilterClass