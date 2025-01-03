from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import ClasificacionImpuesto

from MasterSerializers.serializers_impuestos import ClasificacionImpuestoSerializer

class ClasificacionImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de Padrones"""
    queryset = ClasificacionImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ClasificacionImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ClasificacionImpuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ClasificacionImpuesto
    
    filterset_class = FilterClass