from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.ejecutivoentidad import EjecutivoEntidad

from MasterSerializers.serializers_entidad import EjecutivoEntidadSerializer

class EjecutivoEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = EjecutivoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EjecutivoEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in EjecutivoEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = EjecutivoEntidad
    
    filterset_class = FilterClass