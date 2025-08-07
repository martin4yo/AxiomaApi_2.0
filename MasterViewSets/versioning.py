from rest_framework.versioning import NamespaceVersioning, URLPathVersioning
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render


class AxiomaAPIVersioning(URLPathVersioning):
    """
    Versionado personalizado para AxiomaAPI
    Permite versiones en la URL como /api/v1/ y /api/v2/
    """
    default_version = 'v1'
    allowed_versions = ['v1', 'v2']
    version_param = 'version'


@api_view(['GET'])
def api_version_info(request):
    """
    Endpoint que retorna información de la versión actual
    """
    version = getattr(request, 'version', 'v1')
    
    version_info = {
        'v1': {
            'version': 'v1',
            'description': 'Primera versión de AxiomaAPI',
            'deprecated': False,
            'endpoints_base': '/api/v1/',
            'features': [
                'Gestión de personas y entidades',
                'Productos y precios',
                'Impuestos y contabilidad',
                'Autenticación por token'
            ]
        },
        'v2': {
            'version': 'v2',
            'description': 'Segunda versión de AxiomaAPI con mejoras',
            'deprecated': False,
            'endpoints_base': '/api/v2/',
            'features': [
                'Todas las características de v1',
                'Validación mejorada de tenant',
                'Cache con Redis',
                'Documentación automática',
                'Monitoreo con Silk',
                'Compresión GZIP'
            ]
        }
    }
    
    current_info = version_info.get(version, version_info['v1'])
    
    return Response({
        'current_version': version,
        'api_info': current_info,
        'available_versions': list(version_info.keys())
    })


def version_deprecation_warning(request, version):
    """
    Función para manejar warnings de depreciación de versiones
    """
    deprecated_versions = []  # Agregar versiones deprecadas aquí cuando sea necesario
    
    if version in deprecated_versions:
        return {
            'warning': f'API version {version} is deprecated',
            'message': 'Please upgrade to the latest version',
            'latest_version': 'v2'
        }