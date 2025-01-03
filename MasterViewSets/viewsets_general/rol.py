from MasterViewSets.universal import *

from MasterModels.modelos_general import Rol

from MasterSerializers.serializers_general import RolSerializer

class RolViewSet(GenericModelViewSet):
    """
    ViewSet de Personas
    """
    queryset = Rol.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RolSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Rol._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Rol
    
    filterset_class = FilterClass
