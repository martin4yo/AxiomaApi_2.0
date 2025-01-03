from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import TipoCalculo

from MasterSerializers.serializers_impuestos import TipoCalculoSerializer

class TipoCalculoViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Frecuencia"""
    queryset = TipoCalculo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoCalculoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoCalculo._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoCalculo
    
    filterset_class = FilterClass