from MasterViewSets.universal import *

from MasterModels.modelos_general import TipoResponsable

from MasterSerializers.serializers_general import TipoResponsableSerializer

class TipoResponsableViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Responsable"""
    queryset = TipoResponsable.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoResponsableSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoResponsable._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoResponsable
    
    filterset_class = FilterClass