from MasterViewSets.universal import *

from MasterModels.modelos_general import TipoIndice

from MasterSerializers.serializers_general import TipoIndiceSerializer

class TipoIndiceViewSet(GenericModelViewSet):
    """ ViewSet de CUIT de Paises"""
    queryset = TipoIndice.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoIndiceSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoIndice._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoIndice
    
    filterset_class = FilterClass
