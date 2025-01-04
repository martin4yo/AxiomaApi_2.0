from MasterViewSets.universal import *

from MasterModels.modelos_producto import AtributoValor

from MasterSerializers.serializers_producto import AtributoValorSerializer

class AtributoValorViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = AtributoValor.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AtributoValorSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in AtributoValor._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = AtributoValor
    
    filterset_class = FilterClass