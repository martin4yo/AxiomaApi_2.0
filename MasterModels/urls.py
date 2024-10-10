"""
Urls
"""
from django.urls import path, include
from rest_framework import routers

class Router(routers.DefaultRouter):
    """
    Para PascalName
    """
    pass

router = Router()

# URLS GENERALES

from .api import PersonaViewSet, PersonaRolViewSet, PaisViewSet, ProvinciaViewSet, CodigoPostalViewSet, TipoDeCambioViewSet
from .api import RolViewSet, ModuloViewSet, MascaraViewSet, FormaPagoViewSet, FormaPagoDetalleViewSet
from .api import SectorViewSet, IndiceViewSet, PartidoViewSet, TipoIndiceViewSet, MonedaViewSet, TipoDocumentoViewSet
from .api import TipoFrecuenciaViewSet, TipoValorViewSet, UnidadMedidaViewSet, IncotermsViewSet, TipoResponsableViewSet

router.register('api/general/persona', PersonaViewSet, 'personas')
router.register('api/general/pais', PaisViewSet, 'paises')
router.register('api/general/provincia', ProvinciaViewSet, 'provincias')
router.register('api/general/codigopostal', CodigoPostalViewSet, 'codigospostales')
router.register('api/general/rol', RolViewSet, 'roles')
router.register('api/general/modulo', ModuloViewSet, 'modulos')
router.register('api/general/mascara', MascaraViewSet, 'mascaras')
router.register('api/general/formadepago', FormaPagoViewSet, 'formasdepago')
router.register('api/general/formadepagodetalle', FormaPagoDetalleViewSet, 'formasdepagodetalle')
router.register('api/general/tipodecambio', TipoDeCambioViewSet, 'tiposdecambio')
router.register('api/general/personarol', PersonaRolViewSet, 'personasroles')
router.register('api/general/tipoindice', TipoIndiceViewSet, 'tiposindice')
router.register('api/general/indice', IndiceViewSet, 'indices')
router.register('api/general/partido', PartidoViewSet, 'partidos')
router.register('api/general/sector', SectorViewSet, 'sectores')
router.register('api/general/idioma', IdiomaViewSet, 'idiomas')
router.register('api/general/moneda', MonedaViewSet, 'monedas')
router.register('api/general/tipodocumento', TipoDocumentoViewSet, 'tiposdocumento')
router.register('api/general/tipofrecuencia', TipoFrecuenciaViewSet, 'tiposfrecuencia')
router.register('api/general/tipovalor', TipoValorViewSet, 'tiposvalor')
router.register('api/general/unidadmedida', UnidadMedidaViewSet, 'unidadesmedida')
router.register('api/general/incoterms', IncotermsViewSet, 'incoterms')
router.register('api/general/tiporesponsable', TipoResponsableViewSet, 'tiposresponsable')

# URLS DE IMPUESTOS

from .api import TipoSujetoViewSet, ConceptoIncluidoViewSet
from .api import IdiomaViewSet, TipoComprobanteViewSet
from .api import AlicuotaImpuestoViewSet, PadronImpuestoViewSet
from .api import TipoCalculoViewSet,  ClasificacionImpuestoViewSet
from .api import TipoImpuestoViewSet, CuitPaisViewSet, ImpuestoViewSet

router.register('api/impuestos/tiposujeto', TipoSujetoViewSet, 'tipossujeto')
router.register('api/impuestos/conceptoincluido', ConceptoIncluidoViewSet, 'conceptosincluidos')
router.register('api/impuestos/tipocomprobante', TipoComprobanteViewSet, 'tiposcomprobante')
router.register('api/impuestos/cuitpais', CuitPaisViewSet, 'cuitpaises')
router.register('api/impuestos/alicuotaimpuesto', AlicuotaImpuestoViewSet, 'alicuotasimpuestos')
router.register('api/impuestos/padronimpuesto', PadronImpuestoViewSet, 'padronesimpuesto')
router.register('api/impuestos/tipocalculo', TipoCalculoViewSet, 'tiposcalculo')
router.register('api/impuestos/clasificacionimpuesto', ClasificacionImpuestoViewSet, 'clasificacionesimpuestos')
router.register('api/impuestos/tipoimpuesto', TipoImpuestoViewSet, 'tiposimpuestos')
router.register('api/impuestos/impuesto', ImpuestoViewSet, 'impuestos')

# URLS DE CONTABILIDAD

from .api import TipoAjusteViewSet, PlanCuentasViewSet

router.register('api/contabilidad/tipoajuste', TipoAjusteViewSet, 'tiposajuste')
router.register('api/contabilidad/plandecuentas', PlanCuentasViewSet, 'plandecuentas')

# URLS DE ENTIDADES 

from .api import EntidadViewSet, ZonaViewSet, CondicionCrediticiaViewSet
from .api import ImpuestoEntidadViewSet, EjecutivoViewSet, ContactoEntidadViewSet, TipoSedeViewSet
from .api import TipoDomicilioViewSet, DireccionEntidadViewSet, ModuloEntidadViewSet, SectorEntidadViewSet
from .api import FormaPagoEntidadViewSet

router.register('api/entidades/entidad', EntidadViewSet, 'entidades')
router.register('api/entidades/zona', ZonaViewSet, 'zonas')
router.register('api/entidades/condicioncrediticia', CondicionCrediticiaViewSet, 'condicionescrediticias')
router.register('api/entidades/impuestoentidad', ImpuestoEntidadViewSet, 'impuestosentidad')
router.register('api/entidades/ejecutivo', EjecutivoViewSet, 'ejecutivos')
router.register('api/entidades/contactoentidad', ContactoEntidadViewSet, 'contactosentidad')
router.register('api/entidades/tiposede', TipoSedeViewSet, 'tipossede')
router.register('api/entidades/tipodomicilio', TipoDomicilioViewSet, 'tiposdomicilio')
router.register('api/entidades/direccionentidad', DireccionEntidadViewSet, 'direccionesentidades')
router.register('api/entidades/moduloentidad', ModuloEntidadViewSet, 'modulosentidades')
router.register('api/entidades/sectorentidad', SectorEntidadViewSet, 'sectoresentidades')
router.register('api/entidades/formapagoentidad', FormaPagoEntidadViewSet, 'formaspagoentidades')

# URLS DE PRODUCTOS 

from .api import ListaPreciosViewSet, ListaPrecioEntidadViewSet

router.register('api/productos/listaprecios', ListaPreciosViewSet, 'listasprecios')
router.register('api/productos/listaprecioentidad', ListaPrecioEntidadViewSet, 'listasprecioentidad')

urlpatterns = [
    path('', include(router.urls)),
    # ... otras URLs ...
]
