from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import AlicuotaImpuesto

from MasterSerializers.serializers_impuestos import AlicuotaImpuestoSerializer

class AlicuotaImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = AlicuotaImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AlicuotaImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in AlicuotaImpuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = AlicuotaImpuesto
    
    filterset_class = FilterClass