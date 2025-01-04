from MasterViewSets.universal import *

from MasterModels.modelos_producto import Producto

from MasterSerializers.serializers_producto import ProductoSerializer

class ProductoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = Producto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ProductoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Producto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Producto
    
    filterset_class = FilterClass