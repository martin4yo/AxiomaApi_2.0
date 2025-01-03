from MasterViewSets.universal import *

from MasterModels.modelos_general import Partido

from MasterSerializers.serializers_general import PartidoSerializer

class PartidoViewSet(GenericModelViewSet):
    """ ViewSet de CodigoPostal"""
    queryset = Partido.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PartidoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Partido._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Partido
    
    filterset_class = FilterClass