from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import TipoSujeto

from MasterSerializers.serializers_impuestos import TipoSujetoSerializer


class TipoSujetoViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Sujeto"""
    queryset = TipoSujeto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoSujetoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoSujeto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoSujeto
    
    filterset_class = FilterClass
