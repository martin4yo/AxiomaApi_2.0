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

from MasterViewSets.viewsets_general import PersonaViewSet, PersonaRolViewSet, PaisViewSet, ProvinciaViewSet, CodigoPostalViewSet, TipoCambioViewSet
from MasterViewSets.viewsets_general import RolViewSet, ModuloViewSet, MascaraViewSet, FormaPagoViewSet, FormaPagoDetalleViewSet, IdiomaViewSet
from MasterViewSets.viewsets_general import SectorViewSet, IndiceViewSet, PartidoViewSet, TipoIndiceViewSet, MonedaViewSet, TipoDocumentoViewSet
from MasterViewSets.viewsets_general import TipoFrecuenciaViewSet, TipoValorViewSet, UnidadMedidaViewSet, IncotermsViewSet, TipoResponsableViewSet
from MasterViewSets.viewsets_general import TablasViewSet, TablasConCodigoViewSet

router.register('api/general/persona', PersonaViewSet, 'personas')
router.register('api/general/pais', PaisViewSet, 'paises')
router.register('api/general/provincia', ProvinciaViewSet, 'provincias')
router.register('api/general/codigopostal', CodigoPostalViewSet, 'codigospostales')
router.register('api/general/rol', RolViewSet, 'roles')
router.register('api/general/modulo', ModuloViewSet, 'modulos')
router.register('api/general/mascara', MascaraViewSet, 'mascaras')
router.register('api/general/formapago', FormaPagoViewSet, 'formaspago')
router.register('api/general/formapagodetalle', FormaPagoDetalleViewSet, 'formaspagodetalle')
router.register('api/general/tipocambio', TipoCambioViewSet, 'tiposcambio')
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
router.register('api/general/tablas', TablasViewSet, 'tablas')
router.register('api/general/tablasconcodigo', TablasConCodigoViewSet, 'tablasconcodigo')

# URLS DE IMPUESTOS

from MasterViewSets.viewsets_impuestos import TipoSujetoViewSet, ConceptoIncluidoViewSet
from MasterViewSets.viewsets_impuestos import TipoComprobanteViewSet
from MasterViewSets.viewsets_impuestos import AlicuotaImpuestoViewSet, PadronImpuestoViewSet
from MasterViewSets.viewsets_impuestos import TipoCalculoViewSet,  ClasificacionImpuestoViewSet
from MasterViewSets.viewsets_impuestos import TipoImpuestoViewSet, CuitPaisViewSet, ImpuestoViewSet

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

from MasterViewSets.viewsets_contabilidad import TipoAjusteViewSet, PlanCuentasViewSet

router.register('api/contabilidad/tipoajuste', TipoAjusteViewSet, 'tiposajuste')
router.register('api/contabilidad/plancuentas', PlanCuentasViewSet, 'plancuentas')

# URLS DE ENTIDADES 

from MasterViewSets.viewsets_entidad import EntidadViewSet, ZonaViewSet, CondicionCrediticiaEntidadViewSet
from MasterViewSets.viewsets_entidad import ImpuestoEntidadViewSet, EjecutivoEntidadViewSet, ContactoEntidadViewSet
from MasterViewSets.viewsets_entidad import DireccionEntidadViewSet, ModuloEntidadViewSet, SectorEntidadViewSet
from MasterViewSets.viewsets_entidad import FormaPagoEntidadViewSet, DatosFiscalesEntidadViewSet, ListaPrecioEntidadViewSet

from MasterViewSets.viewsets_general import TipoSedeViewSet, TipoDomicilioViewSet

router.register('api/entidades/entidad', EntidadViewSet, 'entidades')
router.register('api/entidades/zona', ZonaViewSet, 'zonas')
router.register('api/entidades/condicioncrediticiaentidad', CondicionCrediticiaEntidadViewSet, 'condicionescrediticiasentidad')
router.register('api/entidades/impuestoentidad', ImpuestoEntidadViewSet, 'impuestosentidad')
router.register('api/entidades/ejecutivoentidad', EjecutivoEntidadViewSet, 'ejecutivosentidad')
router.register('api/entidades/contactoentidad', ContactoEntidadViewSet, 'contactosentidad')
router.register('api/entidades/tiposede', TipoSedeViewSet, 'tipossede')
router.register('api/entidades/tipodomicilio', TipoDomicilioViewSet, 'tiposdomicilio')
router.register('api/entidades/direccionentidad', DireccionEntidadViewSet, 'direccionesentidad')
router.register('api/entidades/moduloentidad', ModuloEntidadViewSet, 'modulosentidad')
router.register('api/entidades/sectorentidad', SectorEntidadViewSet, 'sectoresentidad')
router.register('api/entidades/formapagoentidad', FormaPagoEntidadViewSet, 'formaspagoentidad')
router.register('api/entidades/datosfiscalesentidad', DatosFiscalesEntidadViewSet, 'datosfiscalesentidad')
router.register('api/productos/listaprecioentidad', ListaPrecioEntidadViewSet, 'listasprecioentidad')

# URLS DE PRODUCTOS 

from MasterViewSets.viewsets_producto import ListaPrecioViewSet, AtributoViewSet, AtributoProductoViewSet, AtributoValorViewSet, AtributoTipoViewSet
from MasterViewSets.viewsets_producto import ClaseProductoViewSet, ContabilidadProductoViewSet, ConversionProductoViewSet
from MasterViewSets.viewsets_producto import ProductoViewSet, TipoProductoViewSet, ListaTipoViewSet, PrecioViewSet


router.register('api/productos/listaprecios', ListaPrecioViewSet, 'listasprecios')
router.register('api/productos/atributo', AtributoViewSet, 'atributos')
router.register('api/productos/atributoproducto', AtributoProductoViewSet, 'atributosproducto')
router.register('api/productos/atributotipo', AtributoTipoViewSet, 'atributostipo')
router.register('api/productos/atributovalor', AtributoValorViewSet, 'atributosvalor')
router.register('api/productos/claseproducto', ClaseProductoViewSet, 'clasesproducto')
router.register('api/productos/contabilidadproducto', ContabilidadProductoViewSet, 'contabilidadproductos')
router.register('api/productos/conversionproducto', ConversionProductoViewSet, 'conversionesproductos')
router.register('api/productos/producto', ProductoViewSet, 'productos')
router.register('api/productos/tipoproducto', TipoProductoViewSet, 'tiposproducto')
router.register('api/productos/listatipo', ListaTipoViewSet, 'listatipos')
router.register('api/productos/precio', PrecioViewSet, 'precios')

# urlpatterns = [
#     path('', include(router.urls)),
#     # ... otras URLs ...
# ]

# VERSIONADO DE API
from MasterViewSets.versioning import api_version_info

# V1 Router (versión actual)
router_v1 = Router()

# Registrar todos los endpoints v1
# URLS GENERALES V1
router_v1.register('general/persona', PersonaViewSet, 'persona')
router_v1.register('general/pais', PaisViewSet, 'pais')
router_v1.register('general/provincia', ProvinciaViewSet, 'provincia')
router_v1.register('general/codigopostal', CodigoPostalViewSet, 'codigopostal')
router_v1.register('general/rol', RolViewSet, 'rol')
router_v1.register('general/modulo', ModuloViewSet, 'modulo')
router_v1.register('general/mascara', MascaraViewSet, 'mascara')
router_v1.register('general/formapago', FormaPagoViewSet, 'formapago')
router_v1.register('general/formapagodetalle', FormaPagoDetalleViewSet, 'formapagodetalle')
router_v1.register('general/tipocambio', TipoCambioViewSet, 'tipocambio')
router_v1.register('general/personarol', PersonaRolViewSet, 'personarol')
router_v1.register('general/tipoindice', TipoIndiceViewSet, 'tipoindice')
router_v1.register('general/indice', IndiceViewSet, 'indice')
router_v1.register('general/partido', PartidoViewSet, 'partido')
router_v1.register('general/sector', SectorViewSet, 'sector')
router_v1.register('general/idioma', IdiomaViewSet, 'idioma')
router_v1.register('general/moneda', MonedaViewSet, 'moneda')
router_v1.register('general/tipodocumento', TipoDocumentoViewSet, 'tipodocumento')
router_v1.register('general/tipofrecuencia', TipoFrecuenciaViewSet, 'tipofrecuencia')
router_v1.register('general/tipovalor', TipoValorViewSet, 'tipovalor')
router_v1.register('general/unidadmedida', UnidadMedidaViewSet, 'unidadmedida')
router_v1.register('general/incoterms', IncotermsViewSet, 'incoterms')
router_v1.register('general/tiporesponsable', TipoResponsableViewSet, 'tiporesponsable')
router_v1.register('general/tablas', TablasViewSet, 'tablas')
router_v1.register('general/tablasconcodigo', TablasConCodigoViewSet, 'tablasconcodigo')

# URLS DE IMPUESTOS V1
router_v1.register('impuestos/tiposujeto', TipoSujetoViewSet, 'tiposujeto')
router_v1.register('impuestos/conceptoincluido', ConceptoIncluidoViewSet, 'conceptoincluido')
router_v1.register('impuestos/tipocomprobante', TipoComprobanteViewSet, 'tipocomprobante')
router_v1.register('impuestos/cuitpais', CuitPaisViewSet, 'cuitpais')
router_v1.register('impuestos/alicuotaimpuesto', AlicuotaImpuestoViewSet, 'alicuotaimpuesto')
router_v1.register('impuestos/padronimpuesto', PadronImpuestoViewSet, 'padronimpuesto')
router_v1.register('impuestos/tipocalculo', TipoCalculoViewSet, 'tipocalculo')
router_v1.register('impuestos/clasificacionimpuesto', ClasificacionImpuestoViewSet, 'clasificacionimpuesto')
router_v1.register('impuestos/tipoimpuesto', TipoImpuestoViewSet, 'tipoimpuesto')
router_v1.register('impuestos/impuesto', ImpuestoViewSet, 'impuesto')

# URLS DE CONTABILIDAD V1
router_v1.register('contabilidad/tipoajuste', TipoAjusteViewSet, 'tipoajuste')
router_v1.register('contabilidad/plancuentas', PlanCuentasViewSet, 'plancuentas')

# URLS DE ENTIDADES V1
router_v1.register('entidades/entidad', EntidadViewSet, 'entidad')
router_v1.register('entidades/zona', ZonaViewSet, 'zona')
router_v1.register('entidades/condicioncrediticiaentidad', CondicionCrediticiaEntidadViewSet, 'condicioncrediticiaentidad')
router_v1.register('entidades/impuestoentidad', ImpuestoEntidadViewSet, 'impuestoentidad')
router_v1.register('entidades/ejecutivoentidad', EjecutivoEntidadViewSet, 'ejecutivoentidad')
router_v1.register('entidades/contactoentidad', ContactoEntidadViewSet, 'contactoentidad')
router_v1.register('entidades/tiposede', TipoSedeViewSet, 'tiposede')
router_v1.register('entidades/tipodomicilio', TipoDomicilioViewSet, 'tipodomicilio')
router_v1.register('entidades/direccionentidad', DireccionEntidadViewSet, 'direccionentidad')
router_v1.register('entidades/moduloentidad', ModuloEntidadViewSet, 'moduloentidad')
router_v1.register('entidades/sectorentidad', SectorEntidadViewSet, 'sectorentidad')
router_v1.register('entidades/formapagoentidad', FormaPagoEntidadViewSet, 'formapagoentidad')
router_v1.register('entidades/datosfiscalesentidad', DatosFiscalesEntidadViewSet, 'datosfiscalesentidad')
router_v1.register('productos/listaprecioentidad', ListaPrecioEntidadViewSet, 'listaprecioentidad')

# URLS DE PRODUCTOS V1
router_v1.register('productos/listaprecios', ListaPrecioViewSet, 'listaprecio')
router_v1.register('productos/atributo', AtributoViewSet, 'atributo')
router_v1.register('productos/atributoproducto', AtributoProductoViewSet, 'atributoproducto')
router_v1.register('productos/atributotipo', AtributoTipoViewSet, 'atributotipo')
router_v1.register('productos/atributovalor', AtributoValorViewSet, 'atributovalor')
router_v1.register('productos/claseproducto', ClaseProductoViewSet, 'claseproducto')
router_v1.register('productos/contabilidadproducto', ContabilidadProductoViewSet, 'contabilidadproducto')
router_v1.register('productos/conversionproducto', ConversionProductoViewSet, 'conversionproducto')
router_v1.register('productos/producto', ProductoViewSet, 'producto')
router_v1.register('productos/tipoproducto', TipoProductoViewSet, 'tipoproducto')
router_v1.register('productos/listatipo', ListaTipoViewSet, 'listatipo')
router_v1.register('productos/precio', PrecioViewSet, 'precio')

# V2 Router (para futuras versiones)
router_v2 = Router()
# Por ahora v2 tiene los mismos endpoints que v1
# En el futuro se pueden agregar nuevos endpoints o modificar existentes
router_v2.registry = router_v1.registry.copy()

# URLS DE AUTENTICACIÓN Y USUARIOS
from MasterViewSets.viewsets_auth import validate_user

urlpatterns = [
    # Mantener compatibilidad con URLs sin versión (defaultea a v1)
    path('', include(router.urls)),
    
    # URLs versionadas
    path('api/v1/', include(router_v1.urls)),
    path('api/v2/', include(router_v2.urls)),
    
    # Información de versión
    path('api/version/', api_version_info, name='api-version'),
    
    # Autenticación (disponible en todas las versiones)
    path('api/auth/validate/', validate_user, name='validate-user'),
    path('api/v1/auth/validate/', validate_user, name='v1-validate-user'),
    path('api/v2/auth/validate/', validate_user, name='v2-validate-user'),
]