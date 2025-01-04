from MasterViewSets.universal import *

from MasterModels.modelos_producto import ContabilidadProducto

from MasterSerializers.serializers_producto import ContabilidadProductoSerializer

class ContabilidadProductoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = ContabilidadProducto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ContabilidadProductoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ContabilidadProducto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ContabilidadProducto
    
    filterset_class = FilterClass