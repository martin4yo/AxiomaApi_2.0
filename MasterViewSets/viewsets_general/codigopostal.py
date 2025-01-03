from MasterViewSets.universal import *

from MasterModels.modelos_general import CodigoPostal

from MasterSerializers.serializers_general import CodigoPostalSerializer

class CodigoPostalViewSet(GenericModelViewSet):
    """ ViewSet de CodigoPostal"""
    queryset = CodigoPostal.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CodigoPostalSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in CodigoPostal._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = CodigoPostal
    
    filterset_class = FilterClass
