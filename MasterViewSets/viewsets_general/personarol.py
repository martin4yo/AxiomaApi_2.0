from MasterViewSets.universal import *

from MasterModels.modelos_general import PersonaRol

from MasterSerializers.serializers_general import PersonaRolSerializer

class PersonaRolViewSet(GenericModelViewSet):
    """
    ViewSet de Roles por Personas
    """
    queryset = PersonaRol.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PersonaRolSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in PersonaRol._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = PersonaRol
    
    filterset_class = FilterClass