# middlewares.py

import logging
from datetime import datetime
import json
import io

logger = logging.getLogger("django")

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obtener los headers de la petición
        headers = {key: value for key, value in request.META.items() if key.startswith('HTTP_')}
        
        # Leer y restaurar el body de la petición
        body = None
        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                request_body = request.body
                request._body = request_body  # Copia para evitar perderlo
                request._stream = io.BytesIO(request_body)  # Restaurar stream
            
                body = json.loads(request_body.decode('utf-8')) if request_body else {}
              
            except json.JSONDecodeError:
                body = request_body.decode('utf-8')  # Si no es JSON, lo guarda como texto

        # Log de la petición
        try:

            logger.info(f"[{datetime.now()}] {request.method} {request.path} - IP: {request.META.get('REMOTE_ADDR')}")
            logger.info(f"Headers: {headers}")
            logger.info(f"Request Body: {body}")

        except Exception as e:
            logger.error(f"Error en la respuesta: {str(e)}")
            raise  # Re-lanzamos el error para que Django lo maneje    


        # Obtener la respuesta llamando al siguiente middleware o vista
        response = self.get_response(request)

        # Leer y loguear la respuesta
        response_body = response.content
        try:
            response_data = json.loads(response_body.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            response_data = response_body.decode('utf-8', errors='ignore')

        logger.info(f"[{datetime.now()}] Respuesta {request.method} {request.path} - Status: {response.status_code}")
        logger.info(f"Response Body: {response_data}")

        return response



class AddCOOPHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        origin = request.headers.get("Origin")
        # Agregar el encabezado COOP
        response['Cross-Origin-Opener-Policy'] = 'unsafe-none'  # Puedes cambiar a 'unsafe-none' si es necesario
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Authorization, Content-Type, X-CSRFToken"
        return response
    

import re 
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied

class DynamicCORSHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        origin = request.headers.get("Origin")
        allowed_pattern = re.compile(r"^http://localhost(:\d+)?$")
        
        if origin and allowed_pattern.match(origin):
            response["Access-Control-Allow-Origin"] = origin
            response["Access-Control-Allow-Credentials"] = "true"
            response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Authorization, Content-Type, X-CSRFToken"

        return response


class TenantValidationMiddleware:
    """
    Middleware para validar tenant_id en requests que lo requieran
    """
    
    EXCLUDED_PATHS = [
        '/admin/',
        '/api/token/',
        '/api/auth/validate/',
    ]
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)
    
    def __call__(self, request):
        # Verificar si la ruta está excluida
        if any(request.path.startswith(path) for path in self.EXCLUDED_PATHS):
            return self.get_response(request)
        
        # Solo validar en rutas de API que no sean de autenticación
        if request.path.startswith('/api/') and request.method in ['POST', 'PUT', 'PATCH']:
            tenant_id = self._extract_tenant_id(request)
            
            if tenant_id is None:
                self.logger.warning(f"Missing tenant_id in request to {request.path}")
                return JsonResponse({
                    'error': 'Missing tenant_id',
                    'message': 'El campo tenant_id es requerido para esta operación'
                }, status=400)
            
            if not self._validate_tenant_id(tenant_id):
                self.logger.warning(f"Invalid tenant_id {tenant_id} in request to {request.path}")
                return JsonResponse({
                    'error': 'Invalid tenant_id',
                    'message': 'El tenant_id proporcionado no es válido'
                }, status=403)
            
            # Agregar tenant_id al request para uso posterior
            request.tenant_id = tenant_id
        
        return self.get_response(request)
    
    def _extract_tenant_id(self, request):
        """Extrae tenant_id del cuerpo de la request o headers"""
        tenant_id = None
        
        # Intentar obtener de headers primero
        tenant_id = request.META.get('HTTP_X_TENANT_ID')
        if tenant_id:
            try:
                return int(tenant_id)
            except ValueError:
                pass
        
        # Intentar obtener del cuerpo de la request
        if hasattr(request, 'data') and 'tenant_id' in request.data:
            try:
                return int(request.data['tenant_id'])
            except (ValueError, TypeError):
                pass
        
        # Para requests POST/PUT con JSON
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
                if 'tenant_id' in data:
                    return int(data['tenant_id'])
            except (json.JSONDecodeError, ValueError, TypeError):
                pass
        
        return None
    
    def _validate_tenant_id(self, tenant_id):
        """Valida que el tenant_id sea válido"""
        if not isinstance(tenant_id, int):
            return False
        
        if tenant_id <= 0:
            return False
        
        # Aquí puedes agregar validaciones adicionales
        # como verificar que el tenant existe en la BD
        
        return True
    
