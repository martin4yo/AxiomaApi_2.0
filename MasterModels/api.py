"""
Api de MasterModels
"""
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Persona, PersonaRol, Pais, Provincia, CodigoPostal
from .models import Rol, Modulo, Mascara, FormaPago, FormaPagoDetalle, TipoDeCambio, Partido, Sector

from .serializers import PersonaSerializer, PersonaRolSerializer, PaisSerializer, ProvinciaSerializer, CodigoPostalSerializer
from .serializers import RolSerializer, ModuloSerializer, MascaraSerializer, FormaPagoSerializer
from .serializers import FormaPagoSerializer, FormaPagoDetalleSerializer, TipoDeCambioSerializer, PartidoSerializer
from .serializers import SectorSerializer

from .filters import PersonaFilter, GenericDynamicFilter, DynamicModelFilter

### VIEWSET BASE #######################################

# class GenericModelViewSet(viewsets.ModelViewSet):
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

class SectorViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = Sector.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SectorSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Sector
    
    filterset_class = FilterClass

class TipoDeCambioViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = TipoDeCambio.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDeCambioSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoDeCambio
    
    filterset_class = FilterClass

class FormaPagoViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaPago.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoSerializer
    
    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPago
    
    filterset_class = FilterClass

class FormaPagoDetalleViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaPagoDetalle.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoDetalleSerializer
    
    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPagoDetalle
    
    filterset_class = FilterClass

class MascaraViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Mascaras
    """
    queryset = Mascara.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MascaraSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Mascara
    
    filterset_class = FilterClass

class ModuloViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Modulos
    """
    queryset = Modulo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ModuloSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Modulo
    
    filterset_class = FilterClass

class RolViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Personas
    """
    queryset = Rol.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RolSerializer

    filter_backends = [DjangoFilterBackend]
    
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

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Persona
    
    filterset_class = FilterClass


class PersonaRolViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Roles por Personas
    """
    queryset = PersonaRol.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PersonaRolSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = PersonaRol
    
    filterset_class = FilterClass


class PaisViewSet(GenericModelViewSet):
    """ ViewSet de Paises"""
   ### queryset = Pais.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PaisSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Pais
    
    filterset_class = FilterClass


class ProvinciaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Provincia"""
    queryset = Provincia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ProvinciaSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Provincia
    
    filterset_class = FilterClass


class CodigoPostalViewSet(viewsets.ModelViewSet):
    """ ViewSet de CodigoPostal"""
    queryset = CodigoPostal.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CodigoPostalSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = CodigoPostal
    
    filterset_class = FilterClass


class PartidoViewSet(viewsets.ModelViewSet):
    """ ViewSet de CodigoPostal"""
    queryset = Partido.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PartidoSerializer

    filter_backends = [DjangoFilterBackend]
    
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

class ImpuestoViewSet(viewsets.ModelViewSet):
    """ ViewSet de  Impuesto"""
    queryset = Impuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImpuestoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPagoDetalle
    
    filterset_class = Impuesto


class TipoImpuestoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Impuesto"""
    queryset = TipoImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoImpuestoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoImpuesto
    
    filterset_class = FilterClass


class TipoCalculoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Frecuencia"""
    queryset = TipoCalculo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoCalculoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoCalculo
    
    filterset_class = FilterClass


class TipoFrecuenciaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Frecuencia"""
    queryset = TipoFrecuencia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoFrecuenciaSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoFrecuencia
    
    filterset_class = FilterClass


class TipoValorViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Valor"""
    queryset = TipoValor.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoValorSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoValor
    
    filterset_class = FilterClass


class MonedaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Monedas"""
    queryset = Moneda.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MonedaSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Moneda
    
    filterset_class = FilterClass


class TipoComprobanteViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Comprobante"""
    queryset = TipoComprobante.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoComprobanteSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoComprobante
    
    filterset_class = FilterClass


class UnidadMedidaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = UnidadMedida.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UnidadMedidaSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = UnidadMedida
    
    filterset_class = FilterClass


class IdiomaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = Idioma.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IdiomaSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Idioma
    
    filterset_class = FilterClass


class IncotermsViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = Incoterms.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IncotermsSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Incoterms
    
    filterset_class = FilterClass


class ConceptoIncluidoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = ConceptoIncluido.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ConceptoIncluidoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ConceptoIncluido
    
    filterset_class = FilterClass


class TipoResponsableViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Responsable"""
    queryset = TipoResponsable.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoResponsableSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoResponsable
    
    filterset_class = FilterClass


class TipoSujetoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Sujeto"""
    queryset = TipoSujeto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoSujetoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoSujeto
    
    filterset_class = FilterClass


class TipoDocumentoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Documento"""
    queryset = TipoDocumento.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDocumentoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoDocumento
    
    filterset_class = FilterClass


class CuitPaisViewSet(viewsets.ModelViewSet):
    """ ViewSet de CUIT de Paises"""
    queryset = CuitPais.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CuitPaisSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = CuitPais
    
    filterset_class = FilterClass


class TipoIndiceViewSet(viewsets.ModelViewSet):
    """ ViewSet de CUIT de Paises"""
    queryset = TipoIndice.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoIndiceSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoIndice
    
    filterset_class = FilterClass


class IndiceViewSet(viewsets.ModelViewSet):
    """ ViewSet de Indices"""
    queryset = Indice.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IndiceSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Indice
    
    filterset_class = FilterClass


class AlicuotaImpuestoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = AlicuotaImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AlicuotaImpuestoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = AlicuotaImpuesto
    
    filterset_class = FilterClass


class PadronImpuestoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Padrones"""
    queryset = PadronImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PadronImpuestoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = PadronImpuesto
    
    filterset_class = FilterClass


class ClasificacionImpuestoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Padrones"""
    queryset = ClasificacionImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ClasificacionImpuestoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ClasificacionImpuesto
    
    filterset_class = FilterClass


### CONTABLE #########################################################
from .models import TipoAjuste, PlanCuentas
from .serializers import TipoaAjusteSerializer, PlanCuentasSerializer

class TipoAjusteViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Ajustes Contables"""
    queryset = TipoAjuste.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoaAjusteSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoAjuste
    
    filterset_class = FilterClass


class PlanCuentasViewSet(viewsets.ModelViewSet):
    """ ViewSet de Plan De Cuentas"""
    queryset = PlanCuentas.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PlanCuentasSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = PlanCuentas
    
    filterset_class = FilterClass



### ENTIDADES #########################################################

from .models import Entidad, Zona, ListaPrecioEntidad, CondicionCrediticia, ImpuestoEntidad, Ejecutivo
from .models import DatosFiscalesEntidad, ContactoEntidad, TipoSede, TipoDomicilio, DireccionEntidad
from .models import ModuloEntidad, SectorEntidad, FormaPagoEntidad

from .serializers import EntidadSerializer, ZonaSerializer, ListaPrecioEntidadSerializer, CondicionCrediticiaSerializer
from .serializers import ImpuestoEntidadSerializer, EjecutivoSerializer, DatosFiscalesEntidadSerializer
from .serializers import ContactoEntidadSerializer, TipoSedeSerializer, TipoDomicilioSerializer, DireccionEntidadSerializer
from .serializers import ModuloEntidadSerializer, SectorEntidadSerializer, FormaPagoEntidadSerializer

class ModuloEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Direcciones de Modulo Entidades"""
    queryset = ModuloEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ModuloEntidadSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ModuloEntidad
    
    filterset_class = FilterClass


class SectorEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Direcciones de Sector Entidades"""
    queryset = SectorEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SectorEntidadSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = SectorEntidad
    
    filterset_class = FilterClass


class FormaPagoEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Direcciones de Forma Pago Entidades"""
    queryset = FormaPagoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoEntidadSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = FormaPagoEntidad
    
    filterset_class = FilterClass


class DireccionEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Direcciones de Entidades"""
    queryset = DireccionEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DireccionEntidadSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = DireccionEntidad
    
    filterset_class = FilterClass

class TipoSedeViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = TipoSede.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoSedeSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoSede
    
    filterset_class = FilterClass


class TipoDomicilioViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = TipoDomicilio.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDomicilioSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = TipoDomicilio
    
    filterset_class = FilterClass


class ContactoEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = ContactoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ContactoEntidadSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ContactoEntidad
    
    filterset_class = FilterClass


class DatosFiscalesEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = DatosFiscalesEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DatosFiscalesEntidadSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = DatosFiscalesEntidad
    
    filterset_class = FilterClass


class EjecutivoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = Ejecutivo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EjecutivoSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Ejecutivo
    
    filterset_class = FilterClass


class ImpuestoEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Impuestos por Entidad"""
    queryset = ImpuestoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImpuestoEntidadSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ImpuestoEntidad
    
    filterset_class = FilterClass


class EntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Entidades"""
    queryset = Entidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EntidadSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Entidad
    
    filterset_class = FilterClass


class ZonaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Zonas"""
    queryset = Zona.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ZonaSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = Zona
    
    filterset_class = FilterClass


class ListaPrecioEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Zonas"""
    queryset = ListaPrecioEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ListaPrecioEntidadSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ListaPrecioEntidad
    
    filterset_class = FilterClass


class CondicionCrediticiaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Condiciones Crediticias"""
    queryset = CondicionCrediticia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CondicionCrediticiaSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = CondicionCrediticia
    
    filterset_class = FilterClass


### PRODUCTOS ##########################################

from .models import ListaPrecios

from .serializers import ListaPreciosSerializer

class ListaPreciosViewSet(viewsets.ModelViewSet):
    """ ViewSet de Entidades"""
    queryset = ListaPrecios.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ListaPreciosSerializer

    filter_backends = [DjangoFilterBackend]
    
    class FilterClass(DynamicModelFilter):
        class Meta(DynamicModelFilter.Meta):
            model = ListaPrecios
    
    filterset_class = FilterClass
