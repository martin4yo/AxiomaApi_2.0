from MasterViewSets.universal import *

from MasterModels.modelos_producto import ListaPrecio

from MasterSerializers.serializers_producto import ListaPrecioSerializer

class ListaPrecioViewSet(GenericModelViewSet):
    """ ViewSet de Entidades"""
    queryset = ListaPrecio.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ListaPrecioSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ListaPrecio._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ListaPrecio
    
    filterset_class = FilterClass
