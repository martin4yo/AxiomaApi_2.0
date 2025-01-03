from MasterViewSets.universal import *

from MasterModels.modelos_general.sector import Sector

from MasterSerializers.serializers_general import SectorSerializer

class SectorViewSet(GenericModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = Sector.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SectorSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Sector._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Sector
    
    filterset_class = FilterClass