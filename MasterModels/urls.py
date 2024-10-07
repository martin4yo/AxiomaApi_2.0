"""
Urls
"""
from django.urls import path, include
from rest_framework import routers

from .api import PersonaViewSet, PersonaRolViewSet, PaisViewSet, ProvinciaViewSet, CodigoPostalViewSet, TipoDeCambioViewSet
from .api import RolViewSet, ModuloViewSet, MascaraViewSet, FormaDePagoViewSet, FormaDePagoDetalleViewSet
from .api import SectorViewSet

from .api import TipoAjusteViewSet, PlanDeCuentasViewSet

from .api import TipoDocumentoViewSet, TipoSujetoViewSet, TipoResponsableViewSet, ConceptoIncluidoViewSet
from .api import IncotermViewSet, IdiomaViewSet, UnidadMedidaViewSet, TipoComprobanteViewSet
from .api import MonedaViewSet, TipoIndiceViewSet, AlicuotaImpuestoViewSet, PadronImpuestoViewSet
from .api import TipoFrecuenciaViewSet, TipoValorViewSet, TipoCalculoViewSet, IndiceViewSet, ClasificacionImpuestoViewSet
from .api import TipoImpuestoViewSet

from .api import ListaPreciosViewSet

from .api import EntidadViewSet, ZonaViewSet, ListaPrecioEntidadViewSet, CondicionCrediticiaViewSet

class Router(routers.DefaultRouter):
    """
    Para PascalName
    """
    pass

router = Router()

# URLS GENERALES
router.register('api/general/persona', PersonaViewSet, 'personas')
router.register('api/general/pais', PaisViewSet, 'paises')
router.register('api/general/provincia', ProvinciaViewSet, 'provincias')
router.register('api/general/codigopostal', CodigoPostalViewSet, 'codigospostales')
router.register('api/general/rol', RolViewSet, 'roles')
router.register('api/general/modulo', ModuloViewSet, 'modulos')
router.register('api/general/mascara', MascaraViewSet, 'mascaras')
router.register('api/general/formadepago', FormaDePagoViewSet, 'formasdepago')
router.register('api/general/formadepagodetalle', FormaDePagoDetalleViewSet, 'formasdepagodetalle')
router.register('api/general/tipodecambio', TipoDeCambioViewSet, 'tiposdecambio')
router.register('api/general/personarol', PersonaRolViewSet, 'personasroles')
router.register('api/general/tipoindice', TipoIndiceViewSet, 'tiposindice')
router.register('api/general/indice', IndiceViewSet, 'indices')
router.register('api/general/partido', IndiceViewSet, 'partidos')
router.register('api/general/sector', SectorViewSet, 'sectores')

# URLS DE IMPUESTOS
router.register('api/taxes/tipodocumento', TipoDocumentoViewSet, 'tiposdocumento')
router.register('api/taxes/tiposujeto', TipoSujetoViewSet, 'tipossujeto')
router.register('api/taxes/tiporesponsable', TipoResponsableViewSet, 'tiposresponsable')
router.register('api/taxes/conceptoincluido', ConceptoIncluidoViewSet, 'conceptosincluidos')
router.register('api/taxes/incoterm', IncotermViewSet, 'incoterms')
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
router.register('api/contabilidad/tipoajuste', TipoAjusteViewSet, 'tiposajuste')
router.register('api/contabilidad/plandecuentas', PlanDeCuentasViewSet, 'plandecuentas')

# URLS DE ENTIDADES 
router.register('api/entidades/entidad', EntidadViewSet, 'entidades')
router.register('api/entidades/zona', ZonaViewSet, 'zonas')
router.register('api/entidades/listaprecioentidad', ListaPrecioEntidadViewSet, 'listasprecioentidad')
router.register('api/entidades/condicioncrediticia', CondicionCrediticiaViewSet, 'condicionescrediticias')

# URLS DE PRODUCTOS 
router.register('api/productos/listaprecios', ListaPreciosViewSet, 'listasprecios')

urlpatterns = [
    path('', include(router.urls)),
    # ... otras URLs ...
]
