from MasterViewSets.universal import *

from MasterModels.modelos_producto import ListaTipo

from MasterSerializers.serializers_producto import ListaTipoSerializer

class ListaTipoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = ListaTipo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ListaTipoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ListaTipo._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ListaTipo
    
    filterset_class = FilterClass