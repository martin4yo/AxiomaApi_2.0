from MasterViewSets.universal import * 

from MasterModels.modelos_entidad.listaprecioentidad import ListaPrecioEntidad

from MasterSerializers.serializers_entidad import ListaPrecioEntidadSerializer

class ListaPrecioEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Zonas"""
    queryset = ListaPrecioEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ListaPrecioEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ListaPrecioEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ListaPrecioEntidad
    
    filterset_class = FilterClass
