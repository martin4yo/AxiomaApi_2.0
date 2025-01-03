from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.condicioncrediticiaentidad import CondicionCrediticiaEntidad

from MasterSerializers.serializers_entidad import CondicionCrediticiaEntidadSerializer

class CondicionCrediticiaEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Condiciones Crediticias"""
    queryset = CondicionCrediticiaEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CondicionCrediticiaEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in CondicionCrediticiaEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = CondicionCrediticiaEntidad
    
    filterset_class = FilterClass