from MasterViewSets.universal import *

from MasterModels.modelos_general import UnidadMedida

from MasterSerializers.serializers_general import UnidadMedidaSerializer

class UnidadMedidaViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = UnidadMedida.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UnidadMedidaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in UnidadMedida._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = UnidadMedida
    
    filterset_class = FilterClass