from MasterViewSets.universal import *

from MasterModels.modelos_general import Indice

from MasterSerializers.serializers_general import IndiceSerializer

class IndiceViewSet(GenericModelViewSet):
    """ ViewSet de Indices"""
    queryset = Indice.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IndiceSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Indice._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Indice
    
    filterset_class = FilterClass
