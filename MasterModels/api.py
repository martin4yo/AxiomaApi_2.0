"""
Api de MasterModels
"""
from rest_framework import viewsets, permissions

from .models import Persona, PersonaRol, Pais, Provincia, CodigoPostal
from .models import Rol, Modulo, Mascara, FormaPago, FormaPagoDetalle, TipoDeCambio, Partido, Sector

from .serializers import PersonaSerializer, PersonaRolSerializer, PaisSerializer, ProvinciaSerializer, CodigoPostalSerializer
from .serializers import RolSerializer, ModuloSerializer, MascaraSerializer, FormaPagoSerializer
from .serializers import FormaPagoSerializer, FormaPagoDetalleSerializer, TipoDeCambioSerializer, PartidoSerializer
from .serializers import SectorSerializer

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

class TipoDeCambioViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = TipoDeCambio.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDeCambioSerializer

class FormaPagoViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaPago.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoSerializer

class FormaPagoDetalleViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaPagoDetalle.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoDetalleSerializer

class MascaraViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Mascaras
    """
    queryset = Mascara.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MascaraSerializer

class MascaraViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Mascaras
    """
    queryset = Mascara.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MascaraSerializer

class ModuloViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Modulos
    """
    queryset = Modulo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ModuloSerializer

class RolViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Personas
    """
    queryset = Rol.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RolSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Personas
    """
    queryset = Persona.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PersonaSerializer

class PersonaRolViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Roles por Personas
    """
    queryset = PersonaRol.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PersonaRolSerializer

class PaisViewSet(viewsets.ModelViewSet):
    """ ViewSet de Paises"""
    queryset = Pais.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PaisSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Provincia"""
    queryset = Provincia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ProvinciaSerializer

class CodigoPostalViewSet(viewsets.ModelViewSet):
    """ ViewSet de CodigoPostal"""
    queryset = CodigoPostal.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CodigoPostalSerializer

class PartidoViewSet(viewsets.ModelViewSet):
    """ ViewSet de CodigoPostal"""
    queryset = Partido.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PartidoSerializer

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

class TipoImpuestoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Impuesto"""
    queryset = TipoImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoImpuestoSerializer

class TipoCalculoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Frecuencia"""
    queryset = TipoCalculo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoCalculoSerializer

class TipoFrecuenciaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Frecuencia"""
    queryset = TipoFrecuencia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoFrecuenciaSerializer

class TipoValorViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Valor"""
    queryset = TipoValor.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoValorSerializer

class MonedaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Monedas"""
    queryset = Moneda.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MonedaSerializer

class TipoComprobanteViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Comprobante"""
    queryset = TipoComprobante.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoComprobanteSerializer

class UnidadMedidaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = UnidadMedida.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UnidadMedidaSerializer

class IdiomaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = Idioma.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IdiomaSerializer

class IncotermsViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = Incoterms.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IncotermsSerializer

class ConceptoIncluidoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = ConceptoIncluido.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ConceptoIncluidoSerializer

class TipoResponsableViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Responsable"""
    queryset = TipoResponsable.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoResponsableSerializer

class TipoSujetoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Sujeto"""
    queryset = TipoSujeto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoSujetoSerializer

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Documento"""
    queryset = TipoDocumento.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDocumentoSerializer

class CuitPaisViewSet(viewsets.ModelViewSet):
    """ ViewSet de CUIT de Paises"""
    queryset = CuitPais.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CuitPaisSerializer

class TipoIndiceViewSet(viewsets.ModelViewSet):
    """ ViewSet de CUIT de Paises"""
    queryset = TipoIndice.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoIndiceSerializer

class IndiceViewSet(viewsets.ModelViewSet):
    """ ViewSet de Indices"""
    queryset = Indice.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IndiceSerializer

class AlicuotaImpuestoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Alicuotas"""
    queryset = AlicuotaImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AlicuotaImpuestoSerializer

class PadronImpuestoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Padrones"""
    queryset = PadronImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PadronImpuestoSerializer

class ClasificacionImpuestoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Padrones"""
    queryset = ClasificacionImpuesto.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ClasificacionImpuestoSerializer

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

class PlanCuentasViewSet(viewsets.ModelViewSet):
    """ ViewSet de Plan De Cuentas"""
    queryset = PlanCuentas.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PlanCuentasSerializer


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

class SectorEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Direcciones de Sector Entidades"""
    queryset = SectorEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SectorEntidadSerializer

class FormaPagoEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Direcciones de Forma Pago Entidades"""
    queryset = FormaPagoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FormaPagoEntidadSerializer

class DireccionEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Direcciones de Entidades"""
    queryset = DireccionEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DireccionEntidadSerializer

class TipoSedeViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = TipoSede.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoSedeSerializer

class TipoDomicilioViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = TipoDomicilio.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TipoDomicilioSerializer

class ContactoEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = ContactoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ContactoEntidadSerializer

class DatosFiscalesEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = DatosFiscalesEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DatosFiscalesEntidadSerializer

class EjecutivoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Ejecutivos"""
    queryset = Ejecutivo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EjecutivoSerializer

class ImpuestoEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Impuestos por Entidad"""
    queryset = ImpuestoEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImpuestoEntidadSerializer

class EntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Entidades"""
    queryset = Entidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EntidadSerializer

class ZonaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Zonas"""
    queryset = Zona.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ZonaSerializer

class ListaPrecioEntidadViewSet(viewsets.ModelViewSet):
    """ ViewSet de Zonas"""
    queryset = ListaPrecioEntidad.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ListaPrecioEntidadSerializer

class CondicionCrediticiaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Condiciones Crediticias"""
    queryset = CondicionCrediticia.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CondicionCrediticiaSerializer

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