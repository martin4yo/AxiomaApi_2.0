from MasterViewSets.universal import *

from MasterModels.modelos_general import Mascara

from MasterSerializers.serializers_general import MascaraSerializer

class MascaraViewSet(GenericModelViewSet):
    """
    ViewSet de Mascaras
    """
    queryset = Mascara.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MascaraSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Mascara._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Mascara
    
    filterset_class = FilterClass
