from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.zona import Zona

from MasterSerializers.serializers_entidad import ZonaSerializer

class ZonaViewSet(GenericModelViewSet):
    """ ViewSet de Zonas"""
    queryset = Zona.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ZonaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Zona._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Zona
    
    filterset_class = FilterClass