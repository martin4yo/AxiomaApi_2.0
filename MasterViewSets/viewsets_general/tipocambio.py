from MasterViewSets.universal import *

from MasterModels.modelos_general import TipoCambio

from MasterSerializers.serializers_general import TipoCambioSerializer

class TipoCambioViewSet(GenericModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = TipoCambio.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoCambioSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoCambio._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoCambio
    
    filterset_class = FilterClass