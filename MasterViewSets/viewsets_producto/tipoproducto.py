from MasterViewSets.universal import *

from MasterModels.modelos_producto import TipoProducto

from MasterSerializers.serializers_producto import TipoProductoSerializer

class TipoProductoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = TipoProducto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoProductoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoProducto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoProducto
    
    filterset_class = FilterClass