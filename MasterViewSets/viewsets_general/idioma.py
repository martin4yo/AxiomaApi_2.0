from MasterViewSets.universal import *

from MasterModels.modelos_general import Idioma

from MasterSerializers.serializers_general import IdiomaSerializer

class IdiomaViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = Idioma.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IdiomaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Idioma._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Idioma
    
    filterset_class = FilterClass
