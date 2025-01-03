from MasterViewSets.universal import * 

from MasterModels.modelos_contabilidad.plancuentas import PlanCuentas
from MasterSerializers.serializers_contabilidad import PlanCuentasSerializer


class PlanCuentasViewSet(GenericModelViewSet):
    """ ViewSet de Plan De Cuentas"""
    queryset = PlanCuentas.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PlanCuentasSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in PlanCuentas._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = PlanCuentas
    
    filterset_class = FilterClass