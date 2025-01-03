from MasterViewSets.universal import *

from MasterModels.modelos_general import Moneda

from MasterSerializers.serializers_general import MonedaSerializer

class MonedaViewSet(GenericModelViewSet):
    """ ViewSet de Monedas"""
    queryset = Moneda.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MonedaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Moneda._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Moneda
    
    filterset_class = FilterClass
