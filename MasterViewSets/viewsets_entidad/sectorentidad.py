from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.sectorentidad import SectorEntidad

from MasterSerializers.serializers_entidad import SectorEntidadSerializer

class SectorEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Direcciones de Sector Entidades"""
    queryset = SectorEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SectorEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in SectorEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = SectorEntidad
    
    filterset_class = FilterClass