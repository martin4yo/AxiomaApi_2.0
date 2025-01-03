from MasterViewSets.universal import *

from MasterModels.modelos_general import Provincia

from MasterSerializers.serializers_general import ProvinciaSerializer

class ProvinciaViewSet(GenericModelViewSet):
    """ ViewSet de Provincia"""
    queryset = Provincia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ProvinciaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Provincia._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Provincia
    
    filterset_class = FilterClass