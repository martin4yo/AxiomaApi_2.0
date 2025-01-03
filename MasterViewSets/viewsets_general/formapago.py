from MasterViewSets.universal import *

from MasterModels.modelos_general import FormaPago

from MasterSerializers.serializers_general import FormaPagoSerializer

class FormaPagoViewSet(GenericModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaPago.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoSerializer
    
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in FormaPago._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPago
    
    filterset_class = FilterClass