from MasterViewSets.universal import *

from MasterModels.modelos_impuestos import ConceptoIncluido

from MasterSerializers.serializers_impuestos import ConceptoIncluidoSerializer

class ConceptoIncluidoViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = ConceptoIncluido.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ConceptoIncluidoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ConceptoIncluido._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ConceptoIncluido
    
    filterset_class = FilterClass
