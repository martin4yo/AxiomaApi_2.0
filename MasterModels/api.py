"""
Api de MasterModels
"""
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .paginators import CustomPagination

from .models import Persona, PersonaRol, Pais, Provincia, CodigoPostal
from .models import Rol, Modulo, Mascara, FormaPago, FormaPagoDetalle, TipoDeCambio, Partido, Sector

from .serializers import PersonaSerializer, PersonaRolSerializer, PaisSerializer, ProvinciaSerializer, CodigoPostalSerializer
from .serializers import RolSerializer, ModuloSerializer, MascaraSerializer, FormaPagoSerializer
from .serializers import FormaPagoSerializer, FormaPagoDetalleSerializer, TipoDeCambioSerializer, PartidoSerializer
from .serializers import SectorSerializer

from .filters import PersonaFilter, GenericDynamicFilter, DynamicModelFilter

### VIEWSET BASE #######################################

# class GenericModelViewSet(GenericModelViewSet):
#     filter_backends = [DjangoFilterBackend]
    
#     def get_queryset(self):
#         # Obtener el modelo del serializer asignado
#         if self.serializer_class.Meta.model is None:
#             raise ValueError("El modelo no se ha pasado al filtro.")
        
#         model = self.serializer_class.Meta.model
#         return model.objects.all()
    
#     def get_filterset(self, request, queryset, view):
#         # Obtiene el modelo del serializer y pasa como argumento al filtro
#         if self.serializer_class.Meta.model is None:
#             raise ValueError("El modelo no se ha pasado al filtro.")
        
#         model = self.serializer_class.Meta.model
#         return GenericDynamicFilter(data=request.GET, queryset=queryset, model=model)

class GenericModelViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = DynamicModelFilter

    def get_queryset(self):
        # Obtener el modelo desde el serializer para definir el queryset
        model = self.serializer_class.Meta.model
        return model.objects.all()

    def get_filterset_class(self):
        # Establece el modelo en el Meta de DynamicModelFilter
        class CustomFilter(DynamicModelFilter):
            class Meta(DynamicModelFilter.Meta):
                model = self.serializer_class.Meta.model
        return CustomFilter

### GENERALES ##########################################

class SectorViewSet(GenericModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = Sector.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SectorSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Sector._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Sector
    
    filterset_class = FilterClass

class TipoDeCambioViewSet(GenericModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = TipoDeCambio.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDeCambioSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoDeCambio._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoDeCambio
    
    filterset_class = FilterClass

class FormaPagoViewSet(GenericModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaPago.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoSerializer
    
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in FormaPago._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPago
    
    filterset_class = FilterClass

class FormaPagoDetalleViewSet(GenericModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaPagoDetalle.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoDetalleSerializer
    
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in FormaPagoDetalle._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPagoDetalle
    
    filterset_class = FilterClass

class MascaraViewSet(GenericModelViewSet):
    """
    ViewSet de Mascaras
    """
    queryset = Mascara.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MascaraSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Mascara._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Mascara
    
    filterset_class = FilterClass

class ModuloViewSet(GenericModelViewSet):
    """
    ViewSet de Modulos
    """
    queryset = Modulo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ModuloSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Modulo._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Modulo
    
    filterset_class = FilterClass

class RolViewSet(GenericModelViewSet):
    """
    ViewSet de Personas
    """
    queryset = Rol.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RolSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Rol._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Rol
    
    filterset_class = FilterClass


class PersonaViewSet(GenericModelViewSet):
    """
    ViewSet de Personas
    """
    serializer_class = PersonaSerializer
    
    queryset = Persona.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Persona._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Persona
    
    filterset_class = FilterClass


class PersonaRolViewSet(GenericModelViewSet):
    """
    ViewSet de Roles por Personas
    """
    queryset = PersonaRol.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PersonaRolSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in PersonaRol._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = PersonaRol
    
    filterset_class = FilterClass


class PaisViewSet(GenericModelViewSet):
    """ ViewSet de Paises"""
    queryset = Pais.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PaisSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Pais._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Pais
    
    filterset_class = FilterClass


class ProvinciaViewSet(GenericModelViewSet):
    """ ViewSet de Provincia"""
    queryset = Provincia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ProvinciaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Provincia._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Provincia
    
    filterset_class = FilterClass


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


class PartidoViewSet(GenericModelViewSet):
    """ ViewSet de CodigoPostal"""
    queryset = Partido.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PartidoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Partido._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Partido
    
    filterset_class = FilterClass

### IMPOSITIVO #########################################################
from .models import TipoDocumento, TipoSujeto, TipoResponsable, ConceptoIncluido, Incoterms, Idioma, UnidadMedida
from .models import TipoComprobante, Moneda, CuitPais, TipoIndice, AlicuotaImpuesto, PadronImpuesto
from .models import TipoFrecuencia, TipoValor, TipoCalculo, Indice, ClasificacionImpuesto, TipoImpuesto
from .models import Impuesto

from .serializers import TipoDocumentoSerializer, TipoSujetoSerializer, TipoResponsableSerializer
from .serializers import ConceptoIncluidoSerializer, IncotermsSerializer, IdiomaSerializer, UnidadMedidaSerializer
from .serializers import TipoComprobanteSerializer, MonedaSerializer, CuitPaisSerializer, TipoIndiceSerializer
from .serializers import AlicuotaImpuestoSerializer, PadronImpuestoSerializer, TipoValorSerializer, TipoFrecuenciaSerializer
from .serializers import TipoCalculoSerializer, IndiceSerializer, ClasificacionImpuestoSerializer, TipoImpuestoSerializer
from .serializers import ImpuestoSerializer

class ImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de  Impuesto"""
    queryset = Impuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Impuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPagoDetalle
    
    filterset_class = Impuesto


class TipoImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Impuesto"""
    queryset = TipoImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoImpuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoImpuesto
    
    filterset_class = FilterClass


class TipoCalculoViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Frecuencia"""
    queryset = TipoCalculo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoCalculoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoCalculo._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoCalculo
    
    filterset_class = FilterClass


class TipoFrecuenciaViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Frecuencia"""
    queryset = TipoFrecuencia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoFrecuenciaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoFrecuencia._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoFrecuencia
    
    filterset_class = FilterClass


class TipoValorViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Valor"""
    queryset = TipoValor.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoValorSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoValor._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoValor
    
    filterset_class = FilterClass


class MonedaViewSet(GenericModelViewSet):
    """ ViewSet de Monedas"""
    queryset = Moneda.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MonedaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Moneda._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Moneda
    
    filterset_class = FilterClass


class TipoComprobanteViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Comprobante"""
    queryset = TipoComprobante.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoComprobanteSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoComprobante._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoComprobante
    
    filterset_class = FilterClass


class UnidadMedidaViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = UnidadMedida.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UnidadMedidaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in UnidadMedida._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = UnidadMedida
    
    filterset_class = FilterClass


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


class TipoResponsableViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Responsable"""
    queryset = TipoResponsable.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoResponsableSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoResponsable._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoResponsable
    
    filterset_class = FilterClass


class TipoSujetoViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Sujeto"""
    queryset = TipoSujeto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoSujetoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoSujeto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoSujeto
    
    filterset_class = FilterClass


class TipoDocumentoViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Documento"""
    queryset = TipoDocumento.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDocumentoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoDocumento._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoDocumento
    
    filterset_class = FilterClass


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


class TipoIndiceViewSet(GenericModelViewSet):
    """ ViewSet de CUIT de Paises"""
    queryset = TipoIndice.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoIndiceSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoIndice._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoIndice
    
    filterset_class = FilterClass


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


class AlicuotaImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = AlicuotaImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AlicuotaImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in AlicuotaImpuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = AlicuotaImpuesto
    
    filterset_class = FilterClass


class PadronImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de Padrones"""
    queryset = PadronImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PadronImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in PadronImpuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = PadronImpuesto
    
    filterset_class = FilterClass


class ClasificacionImpuestoViewSet(GenericModelViewSet):
    """ ViewSet de Padrones"""
    queryset = ClasificacionImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ClasificacionImpuestoSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ClasificacionImpuesto._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ClasificacionImpuesto
    
    filterset_class = FilterClass


### CONTABLE #########################################################
from .models import TipoAjuste, PlanCuentas
from .serializers import TipoaAjusteSerializer, PlanCuentasSerializer

class TipoAjusteViewSet(GenericModelViewSet):
    """ ViewSet de Tipos de Ajustes Contables"""
    queryset = TipoAjuste.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoaAjusteSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoAjuste._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoAjuste
    
    filterset_class = FilterClass


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



### ENTIDADES #########################################################

from .models import Entidad, Zona, ListaPrecioEntidad, CondicionCrediticiaEntidad, ImpuestoEntidad, EjecutivoEntidad
from .models import DatosFiscalesEntidad, ContactoEntidad, TipoSede, TipoDomicilio, DireccionEntidad
from .models import ModuloEntidad, SectorEntidad, FormaPagoEntidad

from .serializers import EntidadSerializer, ZonaSerializer, ListaPrecioEntidadSerializer, CondicionCrediticiaEntidadSerializer
from .serializers import ImpuestoEntidadSerializer, EjecutivoEntidadSerializer, DatosFiscalesEntidadSerializer
from .serializers import ContactoEntidadSerializer, TipoSedeSerializer, TipoDomicilioSerializer, DireccionEntidadSerializer
from .serializers import ModuloEntidadSerializer, SectorEntidadSerializer, FormaPagoEntidadSerializer

class ModuloEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Direcciones de Modulo Entidades"""
    queryset = ModuloEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ModuloEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ModuloEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ModuloEntidad
    
    filterset_class = FilterClass


class SectorEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Direcciones de Sector Entidades"""
    queryset = SectorEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SectorEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in SectorEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = SectorEntidad
    
    filterset_class = FilterClass


class FormaPagoEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Direcciones de Forma Pago Entidades"""
    queryset = FormaPagoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in FormaPagoEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPagoEntidad
    
    filterset_class = FilterClass


class DireccionEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Direcciones de Entidades"""
    queryset = DireccionEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DireccionEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in DireccionEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = DireccionEntidad
    
    filterset_class = FilterClass

class TipoSedeViewSet(GenericModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = TipoSede.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoSedeSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in TipoSede._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoSede
    
    filterset_class = FilterClass


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


class ContactoEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = ContactoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ContactoEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ContactoEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ContactoEntidad
    
    filterset_class = FilterClass


class DatosFiscalesEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = DatosFiscalesEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DatosFiscalesEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in DatosFiscalesEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = DatosFiscalesEntidad
    
    filterset_class = FilterClass


class EjecutivoEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = EjecutivoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EjecutivoEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in EjecutivoEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = EjecutivoEntidad
    
    filterset_class = FilterClass


class ImpuestoEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Impuestos por Entidad"""
    queryset = ImpuestoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImpuestoEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ImpuestoEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ImpuestoEntidad
    
    filterset_class = FilterClass


class EntidadViewSet(GenericModelViewSet):
    """ ViewSet de Entidades"""
    queryset = Entidad.objects.all().prefetch_related(
        'entidad_modulo',  
        'entidad_condicioncrediticia',     
        'entidad_impuesto',     
        'entidad_ejecutivo',     
        'entidad_datosfiscales',     
        'entidad_contacto',     
        'entidad_direcciones',     
        'entidad_sector',     
        'entidad_formapago',     
    )
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Entidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Entidad
    
    filterset_class = FilterClass


class ZonaViewSet(GenericModelViewSet):
    """ ViewSet de Zonas"""
    queryset = Zona.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ZonaSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in Zona._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Zona
    
    filterset_class = FilterClass


class ListaPrecioEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Zonas"""
    queryset = ListaPrecioEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ListaPrecioEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in ListaPrecioEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ListaPrecioEntidad
    
    filterset_class = FilterClass


class CondicionCrediticiaEntidadViewSet(GenericModelViewSet):
    """ ViewSet de Condiciones Crediticias"""
    queryset = CondicionCrediticiaEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CondicionCrediticiaEntidadSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

     # Habilitar todos los campos para ordenamiento
    ordering_fields = [field.name for field in CondicionCrediticiaEntidad._meta.fields]
    ordering = ['id']  # Orden por defecto (clave primaria)
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = CondicionCrediticiaEntidad
    
    filterset_class = FilterClass


### PRODUCTOS ##########################################

from .models import ListaPrecios
from .serializers import ListaPreciosSerializer

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
