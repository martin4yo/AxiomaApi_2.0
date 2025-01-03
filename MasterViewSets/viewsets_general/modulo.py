from MasterViewSets.universal import *

from MasterModels.modelos_general import Modulo

from MasterSerializers.serializers_general import ModuloSerializer

class ModuloViewSet(GenericModelViewSet):
    """
    ViewSet de Modulos
    """
    queryset = Modulo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ModuloSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Modulo._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Modulo
    
    filterset_class = FilterClass