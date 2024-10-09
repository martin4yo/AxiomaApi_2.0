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
from .api import SectorViewSet, IndiceViewSet, PartidoViewSet, TipoIndiceViewSet

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

# URLS DE IMPUESTOS

from .api import TipoDocumentoViewSet, TipoSujetoViewSet, TipoResponsableViewSet, ConceptoIncluidoViewSet
from .api import IncotermsViewSet, IdiomaViewSet, UnidadMedidaViewSet, TipoComprobanteViewSet
from .api import MonedaViewSet, AlicuotaImpuestoViewSet, PadronImpuestoViewSet
from .api import TipoFrecuenciaViewSet, TipoValorViewSet, TipoCalculoViewSet,  ClasificacionImpuestoViewSet
from .api import TipoImpuestoViewSet

router.register('api/taxes/tipodocumento', TipoDocumentoViewSet, 'tiposdocumento')
router.register('api/taxes/tiposujeto', TipoSujetoViewSet, 'tipossujeto')
router.register('api/taxes/tiporesponsable', TipoResponsableViewSet, 'tiposresponsable')
router.register('api/taxes/conceptoincluido', ConceptoIncluidoViewSet, 'conceptosincluidos')
router.register('api/taxes/incoterm', IncotermsViewSet, 'incoterms')
router.register('api/taxes/idioma', IdiomaViewSet, 'idiomas')
router.register('api/taxes/unidadmedida', UnidadMedidaViewSet, 'unidadesmedida')
router.register('api/taxes/tipocomprobante', TipoComprobanteViewSet, 'tiposcomprobante')
router.register('api/taxes/moneda', MonedaViewSet, 'monedas')
router.register('api/taxes/cuitpais', MonedaViewSet, 'cuitpaises')
router.register('api/taxes/alicuotaimpuesto', AlicuotaImpuestoViewSet, 'alicuotasimpuestos')
router.register('api/taxes/padronimpuesto', PadronImpuestoViewSet, 'padronesimpuesto')
router.register('api/taxes/tipofrecuencia', TipoFrecuenciaViewSet, 'tiposfrecuencia')
router.register('api/taxes/tipovalor', TipoValorViewSet, 'tiposvalor')
router.register('api/taxes/tipocalculo', TipoCalculoViewSet, 'tiposcalculo')
router.register('api/taxes/clasificacionimpuesto', ClasificacionImpuestoViewSet, 'clasificacionesimpuestos')
router.register('api/taxes/tipoimpuesto', TipoImpuestoViewSet, 'tiposimpuestos')
router.register('api/taxes/impuesto', TipoImpuestoViewSet, 'impuestos')

# URLS DE CONTABILIDAD

from .api import TipoAjusteViewSet, PlanCuentasViewSet

router.register('api/contabilidad/tipoajuste', TipoAjusteViewSet, 'tiposajuste')
router.register('api/contabilidad/plandecuentas', PlanCuentasViewSet, 'plandecuentas')

# URLS DE ENTIDADES 

from .api import EntidadViewSet, ZonaViewSet, ListaPrecioEntidadViewSet, CondicionCrediticiaViewSet
from .api import ImpuestoEntidadViewSet, EjecutivoViewSet, ContactoEntidadViewSet, TipoSedeViewSet
from .api import TipoDomicilioViewSet, DireccionEntidadViewSet, ModuloEntidadViewSet, SectorEntidadViewSet
from .api import FormaPagoEntidadViewSet

router.register('api/entidades/entidad', EntidadViewSet, 'entidades')
router.register('api/entidades/zona', ZonaViewSet, 'zonas')
router.register('api/entidades/listaprecioentidad', ListaPrecioEntidadViewSet, 'listasprecioentidad')
router.register('api/entidades/condicioncrediticia', CondicionCrediticiaViewSet, 'condicionescrediticias')
router.register('api/entidades/impuestoentidad', ImpuestoEntidadViewSet, 'impuestosentidad')
router.register('api/entidades/ejecutivo', EjecutivoViewSet, 'ejecutivos')
router.register('api/entidades/contactoentidad', ContactoEntidadViewSet, 'contactosentidad')
router.register('api/entidades/tiposede', TipoSedeViewSet, 'tipossede')
router.register('api/entidades/tipodomicilio', TipoDomicilioViewSet, 'tiposdomicilio')
router.register('api/entidades/direccionentidad', DireccionEntidadViewSet, 'direccionesentidades')
router.register('api/entidades/moduloentidad', ModuloEntidadViewSet, 'modulosentidades')
router.register('api/entidades/sectorentidad', SectorEntidadViewSet, 'sectoresentidades')
router.register('api/entidades/formapagoentidad', FormaPagoViewSet, 'formaspagoentidades')

# URLS DE PRODUCTOS 

from .api import ListaPreciosViewSet

router.register('api/productos/listaprecios', ListaPreciosViewSet, 'listasprecios')

urlpatterns = [
    path('', include(router.urls)),
    # ... otras URLs ...
]
