from MasterViewSets.universal import *

from MasterModels.modelos_general import Pais

from MasterSerializers.serializers_general import PaisSerializer

class PaisViewSet(GenericModelViewSet):
    """ ViewSet de Paises"""
    queryset = Pais.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PaisSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Pais._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Pais
    
    filterset_class = FilterClass