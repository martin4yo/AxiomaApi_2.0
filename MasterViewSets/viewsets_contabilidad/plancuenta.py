from MasterViewSets.universal import * 

from MasterModels.modelos_contabilidad.plancuenta import PlanCuenta
from MasterSerializers.serializers_contabilidad import PlanCuentaSerializer


class PlanCuentasViewSet(GenericModelViewSet):
    """ ViewSet de Plan De Cuentas"""
    queryset = PlanCuenta.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PlanCuentaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in PlanCuenta._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = PlanCuenta
    
    filterset_class = FilterClass