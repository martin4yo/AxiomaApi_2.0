from MasterViewSets.universal import *

from MasterModels.modelos_producto import AtributoTipo

from MasterSerializers.serializers_producto import AtributoTipoSerializer

class AtributoTipoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = AtributoTipo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AtributoTipo

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in AtributoTipo._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = AtributoTipo
    
    filterset_class = FilterClass