from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import CuitPais

from MasterSerializers.serializers_impuestos import CuitPaisSerializer

class CuitPaisViewSet(GenericModelViewSet):
    """ ViewSet de CUIT de Paises"""
    queryset = CuitPais.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CuitPaisSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in CuitPais._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = CuitPais
    
    filterset_class = FilterClass

