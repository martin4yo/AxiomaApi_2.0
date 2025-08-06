# AxiomaAPI 2.0 - Análisis y Documentación

## Resumen del Proyecto

**AxiomaAPI 2.0** es una API REST desarrollada con **Python 3.12**, **Django 5.1.2** y **Django REST Framework 3.15.2**, diseñada como backend para un sistema ERP. La API expone tablas comerciales y datos maestros para ser consumidos por un frontend desarrollado por separado.

## Arquitectura del Proyecto

### Estructura de Directorios

```
AxiomaApi_2.0/
├── AxiomaConnect/          # Configuración principal del proyecto Django
│   ├── settings.py         # Configuración principal
│   ├── urls.py            # URLs principales
│   ├── middlewares.py     # Middlewares personalizados
│   └── wsgi.py/asgi.py    # Servidores WSGI/ASGI
├── MasterModels/          # Modelos de datos organizados por dominio
│   ├── modelos_contabilidad/
│   ├── modelos_entidad/
│   ├── modelos_general/
│   ├── modelos_impuestos/
│   ├── modelos_producto/
│   ├── universal.py       # Modelos base abstractos
│   └── paginators.py      # Paginación personalizada
├── MasterSerializers/     # Serializers organizados por dominio
│   ├── serializers_contabilidad/
│   ├── serializers_entidad/
│   ├── serializers_general/
│   ├── serializers_impuestos/
│   └── serializers_producto/
├── MasterViewSets/        # ViewSets y lógica de API
│   ├── viewsets_contabilidad/
│   ├── viewsets_entidad/
│   ├── viewsets_general/
│   ├── viewsets_impuestos/
│   ├── viewsets_producto/
│   ├── viewsets_auth/     # Autenticación personalizada
│   ├── api.py            # Clases base para ViewSets
│   ├── universal.py      # Imports comunes
│   └── urls.py           # Configuración de rutas API
└── static/               # Archivos estáticos
```

### Patrones de Diseño Implementados

1. **Arquitectura Modular**: Separación clara entre modelos, serializers y viewsets
2. **Multitenant**: Soporte para múltiples inquilinos con `tenant_id`
3. **Auditoría**: Modelos base con campos de auditoría (`AuditModel`)
4. **DRY (Don't Repeat Yourself)**: Uso de clases base y herencia
5. **RESTful API**: Endpoints siguiendo convenciones REST

## Análisis Técnico

### Tecnologías y Dependencias

```python
# requirements.txt principales
Django==5.1.2
djangorestframework==3.15.2
django-cors-headers==4.6.0
django-filter==24.3
django-jazzmin==3.0.1
mysqlclient==2.2.5
python-decouple==3.8
```

### Configuración de Seguridad (settings.py:25-31)

**⚠️ PROBLEMAS DE SEGURIDAD CRÍTICOS IDENTIFICADOS:**

1. **DEBUG habilitado en producción**:
   ```python
   DEBUG = True  # Línea 29
   ```

2. **ALLOWED_HOSTS permisivo**:
   ```python
   ALLOWED_HOSTS = ['*']  # Línea 31
   ```

3. **Contraseña por defecto en código**:
   ```python
   'PASSWORD': config('DB_PASSWORD', default='Axioma2024!')  # Línea 130
   ```

### Modelos de Datos

#### Modelos Base (`universal.py:8-24`)

```python
class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)
    user_id = models.ForeignKey('Persona', on_delete=models.CASCADE, blank=True, null=True)

class TenantModel(models.Model):
    tenant_id = models.BigIntegerField(blank=True, null=True)
```

#### Estructura de Dominios

- **General**: Entidades base (Persona, País, Moneda, etc.)
- **Productos**: Catálogo de productos, precios, atributos
- **Entidades**: Clientes, proveedores, contactos
- **Impuestos**: Configuración fiscal y tributaria
- **Contabilidad**: Plan de cuentas y ajustes contables

### API Endpoints

La API expone **47 endpoints principales** organizados por dominio:

- `/api/general/*` - 18 endpoints de datos maestros
- `/api/productos/*` - 12 endpoints de productos
- `/api/entidades/*` - 13 endpoints de entidades comerciales
- `/api/impuestos/*` - 10 endpoints de configuración fiscal
- `/api/contabilidad/*` - 2 endpoints contables
- `/api/auth/validate/` - Endpoint de autenticación personalizada

### Middlewares Personalizados (`middlewares.py`)

1. **LogRequestMiddleware**: Logging detallado de requests/responses
2. **DynamicCORSHeadersMiddleware**: CORS dinámico para localhost
3. **AddCOOPHeaderMiddleware**: Headers de política COOP

### Autenticación (`viewsets_auth/auth_user.py`)

Sistema de validación de usuarios personalizado que soporta:
- Validación GET y POST
- Respuestas estructuradas con códigos de error
- Verificación de estado de usuario (activo/inactivo)

## Mejoras Recomendadas

### 🔴 Críticas (Seguridad)

1. **Configurar entorno de producción**:
   ```python
   # En settings.py
   DEBUG = config('DEBUG', default=False, cast=bool)
   ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')
   ```

2. **Eliminar credenciales por defecto**:
   ```python
   # Remover valores por defecto de BD
   'PASSWORD': config('DB_PASSWORD')  # Sin default
   SECRET_KEY = config('SECRET_KEY')  # Sin default
   ```

3. **Implementar validación de tenant**:
   ```python
   # Middleware para validar tenant_id en requests
   class TenantValidationMiddleware
   ```

### 🟡 Importantes (Funcionalidad)

1. **Documentación API automática**:
   ```python
   # Agregar drf-spectacular
   pip install drf-spectacular
   ```

2. **Validaciones de modelo mejoradas**:
   ```python
   # En modelos, agregar validadores personalizados
   def validate_codigo_unique_per_tenant(self):
   ```

3. **Cache y Performance**:
   ```python
   # Implementar Redis para caching
   CACHES = {
       'default': {
           'BACKEND': 'django_redis.cache.RedisCache',
           'LOCATION': config('REDIS_URL'),
       }
   }
   ```

4. **Tests unitarios**:
   ```bash
   # Crear estructura de tests
   mkdir tests/
   ```

### 🟢 Mejoras Opcionales

1. **Versionado de API**:
   ```python
   # Implementar versionado: /api/v1/, /api/v2/
   ```

2. **Compresión de respuestas**:
   ```python
   # Middleware de compresión GZIP
   'django.middleware.gzip.GZipMiddleware'
   ```

3. **Monitoreo y métricas**:
   ```python
   # Implementar Django-silk o similar
   ```

## Comandos de Desarrollo

```bash
# Servidor de desarrollo
python manage.py runserver

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recolectar archivos estáticos
python manage.py collectstatic
```

## Estructura de URLs

```
/admin/                    # Admin de Django (Jazzmin)
/api/token/               # Obtener token de autenticación
/api/auth/validate/       # Validación personalizada de usuarios
/api/general/            # Endpoints de datos maestros
/api/productos/          # Endpoints de productos
/api/entidades/          # Endpoints de entidades comerciales
/api/impuestos/          # Endpoints de configuración fiscal
/api/contabilidad/       # Endpoints contables
```

## Logging

Sistema de logging configurado con rotación diaria:
- Archivos: `logs/YYYYMMDD.log`
- Rotación: Medianoche
- Retención: 7 días
- Nivel: INFO

## Consideraciones de Despliegue

### Base de Datos
- **Desarrollo**: SQLite (para pruebas rápidas)
- **Producción**: MySQL 8.0+ (configurado)

### Variables de Entorno Requeridas
```bash
SECRET_KEY=tu-secret-key-super-segura
DEBUG=False
DB_NAME=axiomaconnect
DB_USER=tu-usuario
DB_PASSWORD=tu-password-segura
DB_HOST=localhost
DB_PORT=3306
STATIC_ROOT=/path/to/static/
DJANGO_ENV=production
```

### Servidor Web Recomendado
- **Gunicorn** + **Nginx** para producción
- **WhiteNoise** para servir archivos estáticos (alternativa simple)

## Estado del Código

✅ **Fortalezas:**
- Arquitectura modular bien organizada
- Separación clara de responsabilidades
- Soporte multitenant implementado
- API RESTful completa
- Logging estructurado
- CORS configurado correctamente

⚠️ **Áreas de Mejora:**
- Configuración de seguridad crítica
- Falta de tests automatizados
- Sin documentación automática de API
- Validaciones de negocio limitadas
- Sin sistema de cache implementado

## Próximos Pasos Recomendados

1. **Inmediato**: Corregir problemas de seguridad críticos
2. **Corto plazo**: Implementar tests y documentación API
3. **Mediano plazo**: Optimizar performance y agregar cache
4. **Largo plazo**: Implementar monitoreo y métricas avanzadas

---

*Documentación generada por Claude Code el 2025-08-06*