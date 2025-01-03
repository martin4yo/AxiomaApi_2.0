from MasterViewSets.universal import *

from MasterModels.modelos_general import Incoterms

from MasterSerializers.serializers_general import IncotermsSerializer

class IncotermsViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = Incoterms.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IncotermsSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Incoterms._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Incoterms
    
    filterset_class = FilterClass