from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import TipoImpuesto

from MasterSerializers.serializers_impuestos import TipoImpuestoSerializer

class TipoImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Impuesto"""
    queryset = TipoImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoImpuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoImpuesto
    
    filterset_class = FilterClass
