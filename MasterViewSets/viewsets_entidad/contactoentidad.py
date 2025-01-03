from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.contactoentidad import ContactoEntidad

from MasterSerializers.serializers_entidad import ContactoEntidadSerializer


class ContactoEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = ContactoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ContactoEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ContactoEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ContactoEntidad
    
    filterset_class = FilterClass