from rest_framework import permissions
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from MasterModels.paginators import CustomPagination
from MasterViewSets.api import GenericModelViewSet 
from MasterViewSets.api import DynamicModelFilter 

from MasterModels.modelos_producto import ListaPrecios
from MasterSerializers.serializers_producto import ListaPreciosSerializer

class ListaPreciosViewSet(GenericModelViewSet):
    """ ViewSet de Entidades"""
    queryset = ListaPrecios.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ListaPreciosSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ListaPrecios._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ListaPrecios
    
    filterset_class = FilterClass
