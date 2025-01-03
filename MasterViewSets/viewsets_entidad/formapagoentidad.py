from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.formapagoentidad import FormaPagoEntidad

from MasterSerializers.serializers_entidad import FormaPagoEntidadSerializer


class FormaPagoEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Direcciones de Forma Pago Entidades"""
    queryset = FormaPagoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in FormaPagoEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPagoEntidad
    
    filterset_class = FilterClass