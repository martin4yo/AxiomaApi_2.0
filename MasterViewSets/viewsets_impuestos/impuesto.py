from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import Impuesto

from MasterSerializers.serializers_impuestos import ImpuestoSerializer

class ImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de  Impuesto"""
    queryset = Impuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Impuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Impuesto
    
    filterset_class = FilterClass

