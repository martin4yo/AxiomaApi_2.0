from MasterViewSets.universal import *

from MasterModels.modelos_producto import Atributo

from MasterSerializers.serializers_producto import AtributoSerializer

class AtributoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = Atributo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AtributoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Atributo._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Atributo
    
    filterset_class = FilterClass