from MasterViewSets.universal import * 

from MasterModels.modelos_contabilidad.tipoajuste import TipoAjuste
from MasterSerializers.serializers_contabilidad.tipoajuste import TipoaAjusteSerializer

class TipoAjusteViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Ajustes Contables"""
    queryset = TipoAjuste.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoaAjusteSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoAjuste._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoAjuste
    
    filterset_class = FilterClass