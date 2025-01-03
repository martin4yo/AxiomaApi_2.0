from MasterViewSets.universal import *

from MasterModels.modelos_general import FormaPagoDetalle

from MasterSerializers.serializers_general import FormaPagoDetalleSerializer

class FormaPagoDetalleViewSet(GenericModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaPagoDetalle.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoDetalleSerializer
    
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in FormaPagoDetalle._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPagoDetalle
    
    filterset_class = FilterClass
