from MasterViewSets.universal import *

from MasterModels.modelos_producto import ClaseProducto

from MasterSerializers.serializers_producto import ClaseProductoSerializer

class ClaseProductoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = ClaseProducto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ClaseProductoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ClaseProducto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ClaseProducto
    
    filterset_class = FilterClass