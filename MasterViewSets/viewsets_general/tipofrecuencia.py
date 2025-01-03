from MasterViewSets.universal import *

from MasterModels.modelos_general import TipoFrecuencia

from MasterSerializers.serializers_general import TipoFrecuenciaSerializer

class TipoFrecuenciaViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Frecuencia"""
    queryset = TipoFrecuencia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoFrecuenciaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoFrecuencia._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoFrecuencia
    
    filterset_class = FilterClass