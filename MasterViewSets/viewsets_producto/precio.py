from MasterViewSets.universal import *

from MasterModels.modelos_producto import Precio

from MasterSerializers.serializers_producto import PrecioSerializer

class PrecioViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = Precio.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PrecioSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Precio._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Precio
    
    filterset_class = FilterClass