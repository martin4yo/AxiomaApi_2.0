from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.direccionentidad import DireccionEntidad

from MasterSerializers.serializers_entidad import DireccionEntidadSerializer


class DireccionEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Direcciones de Entidades"""
    queryset = DireccionEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DireccionEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in DireccionEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = DireccionEntidad
    
    filterset_class = FilterClass