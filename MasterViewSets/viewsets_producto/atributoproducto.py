from MasterViewSets.universal import *

from MasterModels.modelos_producto import AtributoProducto

from MasterSerializers.serializers_producto import AtributoProductoSerializer

class AtributoProductoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = AtributoProducto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AtributoProducto

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in AtributoProducto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = AtributoProducto
    
    filterset_class = FilterClass