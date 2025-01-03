from MasterViewSets.universal import *

from MasterModels.modelos_general import TipoValor

from MasterSerializers.serializers_general import TipoValorSerializer

class TipoValorViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Valor"""
    queryset = TipoValor.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoValorSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoValor._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoValor
    
    filterset_class = FilterClass
