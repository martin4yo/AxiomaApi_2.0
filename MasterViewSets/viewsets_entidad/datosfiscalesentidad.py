from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.datosfiscalesentidad import DatosFiscalesEntidad

from MasterSerializers.serializers_entidad import DatosFiscalesEntidadSerializer

class DatosFiscalesEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = DatosFiscalesEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DatosFiscalesEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in DatosFiscalesEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = DatosFiscalesEntidad
    
    filterset_class = FilterClass