from MasterViewSets.universal import *

from MasterModels.modelos_general import TipoSede

from MasterSerializers.serializers_general import TipoSedeSerializer

class TipoSedeViewSet(GenericModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = TipoSede.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoSedeSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoSede._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoSede
    
    filterset_class = FilterClass