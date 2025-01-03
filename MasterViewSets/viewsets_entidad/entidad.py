from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.entidad import Entidad

from MasterSerializers.serializers_entidad import EntidadSerializer

class EntidadViewSet(GenericModelViewSet):
    """ ViewSet de Entidades"""
    queryset = Entidad.objects.all().prefetch_related(
        'entidad_modulo',  
        'entidad_condicioncrediticia',     
        'entidad_impuesto',     
        'entidad_ejecutivo',     
        'entidad_datosfiscales',     
        'entidad_contacto',     
        'entidad_direcciones',     
        'entidad_sector',     
        'entidad_formapago',     
    )
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Entidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Entidad
    
    filterset_class = FilterClass
