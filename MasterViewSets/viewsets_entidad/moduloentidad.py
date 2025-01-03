from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.moduloentidad import ModuloEntidad

from MasterSerializers.serializers_entidad import ModuloEntidadSerializer

class ModuloEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Direcciones de Modulo Entidades"""
    queryset = ModuloEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ModuloEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ModuloEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ModuloEntidad
    
    filterset_class = FilterClass