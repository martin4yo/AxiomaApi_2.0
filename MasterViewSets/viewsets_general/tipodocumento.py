from MasterViewSets.universal import *

from MasterModels.modelos_general import TipoDocumento

from MasterSerializers.serializers_general import TipoDocumentoSerializer

class TipoDocumentoViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Documento"""
    queryset = TipoDocumento.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDocumentoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoDocumento._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoDocumento
    
    filterset_class = FilterClass