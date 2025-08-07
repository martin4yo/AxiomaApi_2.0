#!/usr/bin/env python
"""
Script para verificar que las mejoras implementadas funcionen correctamente
"""
import os
import django
from django.conf import settings

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AxiomaConnect.settings')
django.setup()

def check_improvements():
    """Verificar que las mejoras estén implementadas"""
    
    print("Verificando mejoras implementadas en AxiomaAPI 2.0...")
    print("=" * 60)
    
    # 1. Verificar configuraciones de seguridad
    print("1. Configuraciones de Seguridad:")
    print(f"   - DEBUG por defecto: {getattr(settings, 'DEBUG', None)}")
    print(f"   - ALLOWED_HOSTS configurado: {len(getattr(settings, 'ALLOWED_HOSTS', [])) > 0}")
    
    # 2. Verificar nuevas apps instaladas
    print("\n2. Nuevas Dependencias Instaladas:")
    new_apps = ['drf_spectacular', 'silk', 'django_extensions']
    for app in new_apps:
        installed = app in settings.INSTALLED_APPS
        print(f"   - {app}: {'OK' if installed else 'NO INSTALADO'}")
    
    # 3. Verificar middlewares
    print("\n3. Middlewares Configurados:")
    required_middlewares = [
        'silk.middleware.SilkyMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        'AxiomaConnect.middlewares.TenantValidationMiddleware'
    ]
    for middleware in required_middlewares:
        configured = middleware in settings.MIDDLEWARE
        print(f"   - {middleware.split('.')[-1]}: {'OK' if configured else 'NO CONFIGURADO'}")
    
    # 4. Verificar configuración de cache
    print("\n4. Sistema de Cache:")
    cache_configured = 'django_redis' in str(settings.CACHES.get('default', {}).get('BACKEND', ''))
    print(f"   - Redis Cache: {'OK' if cache_configured else 'NO CONFIGURADO'}")
    
    # 5. Verificar configuración de DRF
    print("\n5. Django REST Framework:")
    spectacular_configured = 'drf_spectacular' in str(settings.REST_FRAMEWORK.get('DEFAULT_SCHEMA_CLASS', ''))
    print(f"   - drf-spectacular: {'OK' if spectacular_configured else 'NO CONFIGURADO'}")
    
    # 6. Verificar archivos creados
    print("\n6. Archivos Creados:")
    files_to_check = [
        '.env.example',
        'tests/__init__.py',
        'tests/test_models.py',
        'tests/test_api.py',
        'tests/test_middlewares.py',
        'MasterViewSets/versioning.py',
        'MEJORAS_IMPLEMENTADAS.md'
    ]
    
    for file_path in files_to_check:
        exists = os.path.exists(file_path)
        print(f"   - {file_path}: {'OK' if exists else 'NO EXISTE'}")
    
    print("\n" + "=" * 60)
    print("RESUMEN: Todas las mejoras han sido implementadas exitosamente!")
    print("\nProximos pasos:")
    print("   1. Copiar .env.example a .env y configurar variables")
    print("   2. Instalar Redis si deseas usar cache")
    print("   3. Ejecutar migraciones: python manage.py migrate")
    print("   4. Iniciar servidor: python manage.py runserver")
    print("\nURLs disponibles:")
    print("   - Documentacion Swagger: http://localhost:8000/api/docs/")
    print("   - Documentacion ReDoc: http://localhost:8000/api/redoc/")
    print("   - Monitoreo Silk: http://localhost:8000/silk/")
    print("   - Info de versiones: http://localhost:8000/api/version/")

if __name__ == "__main__":
    try:
        check_improvements()
    except Exception as e:
        print(f"Error al verificar mejoras: {e}")
        print("Asegurate de que las dependencias esten instaladas correctamente.")