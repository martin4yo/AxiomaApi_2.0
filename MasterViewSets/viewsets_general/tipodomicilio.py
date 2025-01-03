from MasterViewSets.universal import *

from MasterModels.modelos_general.tipodomicilio import TipoDomicilio

from MasterSerializers.serializers_general import TipoDomicilioSerializer

class TipoDomicilioViewSet(GenericModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = TipoDomicilio.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDomicilioSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoDomicilio._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoDomicilio
    
    filterset_class = FilterClass
