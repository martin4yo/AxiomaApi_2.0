from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.impuestoentidad import ImpuestoEntidad

from MasterSerializers.serializers_entidad import ImpuestoEntidadSerializer

class ImpuestoEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Impuestos por Entidad"""
    queryset = ImpuestoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImpuestoEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ImpuestoEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ImpuestoEntidad
    
    filterset_class = FilterClass