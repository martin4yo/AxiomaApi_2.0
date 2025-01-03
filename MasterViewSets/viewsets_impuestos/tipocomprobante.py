from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import TipoComprobante

from MasterSerializers.serializers_impuestos import TipoComprobanteSerializer

class TipoComprobanteViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Comprobante"""
    queryset = TipoComprobante.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoComprobanteSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoComprobante._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoComprobante
    
    filterset_class = FilterClass
