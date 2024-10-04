"""
Api de MasterModels
"""
from rest_framework import viewsets, permissions

from .models import Persona, PersonaRol, Pais, Provincia, CodigoPostal
from .models import Rol, Modulo, Mascara, FormaDePago, FormaDePagoDetalle, TipoDeCambio

from .serializers import PersonaSerializer, PersonaRolSerializer, PaisSerializer, ProvinciaSerializer, CodigoPostalSerializer
from .serializers import RolSerializer, ModuloSerializer, MascaraSerializer, FormaDePagoSerializer
from .serializers import FormaDePagoSerializer, FormaDePagoDetalleSerializer, TipoDeCambioSerializer

### GENERALES ##########################################

class TipoDeCambioViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = TipoDeCambio.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoDeCambioSerializer

class FormaDePagoViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaDePago.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FormaDePagoSerializer

class FormaDePagoDetalleViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Formas de Pago
    """
    queryset = FormaDePagoDetalle.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FormaDePagoDetalleSerializer

class MascaraViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Mascaras
    """
    queryset = Mascara.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MascaraSerializer

class MascaraViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Mascaras
    """
    queryset = Mascara.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MascaraSerializer

class ModuloViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Modulos
    """
    queryset = Modulo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ModuloSerializer

class RolViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Personas
    """
    queryset = Rol.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RolSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Personas
    """
    queryset = Persona.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PersonaSerializer

class PersonaRolViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Roles por Personas
    """
    queryset = PersonaRol.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PersonaRolSerializer

class PaisViewSet(viewsets.ModelViewSet):
    """ ViewSet de Paises"""
    queryset = Pais.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PaisSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Provincia"""
    queryset = Provincia.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProvinciaSerializer

class CodigoPostalViewSet(viewsets.ModelViewSet):
    """ ViewSet de CodigoPostal"""
    queryset = CodigoPostal.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CodigoPostalSerializer

### IMPOSITIVO #########################################################
from .models import TipoDocumento, TipoSujeto, TipoResponsable, ConceptoIncluido, Incoterm, Idioma, UnidadMedida
from .models import TipoComprobante, Moneda, CuitPais, TipoIndice
from .serializers import TipoDocumentoSerializer, TipoSujetoSerializer, TipoResponsableSerializer
from .serializers import ConceptoIncluidoSerializer, IncotermSerializer, IdiomaSerializer, UnidadMedidaSerializer
from .serializers import TipoComprobanteSerializer, MonedaSerializer, CuitPaisSerializer, TipoIndiceSerializer

class MonedaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Monedas"""
    queryset = Moneda.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MonedaSerializer

class TipoComprobanteViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Comprobante"""
    queryset = TipoComprobante.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoComprobanteSerializer

class UnidadMedidaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = UnidadMedida.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UnidadMedidaSerializer

class IdiomaViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = Idioma.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IdiomaSerializer

class IncotermViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = Incoterm.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IncotermSerializer

class ConceptoIncluidoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Conceptos de AFIP"""
    queryset = ConceptoIncluido.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ConceptoIncluidoSerializer

class TipoResponsableViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Responsable"""
    queryset = TipoResponsable.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoResponsableSerializer

class TipoSujetoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Sujeto"""
    queryset = TipoSujeto.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoSujetoSerializer

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Documento"""
    queryset = TipoDocumento.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoDocumentoSerializer

class CuitPaisViewSet(viewsets.ModelViewSet):
    """ ViewSet de CUIT de Paises"""
    queryset = CuitPais.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CuitPaisSerializer

class TipoIndiceViewSet(viewsets.ModelViewSet):
    """ ViewSet de CUIT de Paises"""
    queryset = TipoIndice.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoIndiceSerializer

### CONTABLE #########################################################
from .models import TipoAjuste, PlanDeCuentas
from .serializers import TipoaAjusteSerializer, PlanDeCuentasSerializer

class TipoAjusteViewSet(viewsets.ModelViewSet):
    """ ViewSet de Tipos de Ajustes Contables"""
    queryset = TipoAjuste.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoaAjusteSerializer

class PlanDeCuentasViewSet(viewsets.ModelViewSet):
    """ ViewSet de Plan De Cuentas"""
    queryset = PlanDeCuentas.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlanDeCuentasSerializer