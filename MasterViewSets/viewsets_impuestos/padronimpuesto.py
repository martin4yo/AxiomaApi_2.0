from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import PadronImpuesto

from MasterSerializers.serializers_impuestos import PadronImpuestoSerializer

class PadronImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de Padrones"""
    queryset = PadronImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PadronImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in PadronImpuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = PadronImpuesto
    
    filterset_class = FilterClass
