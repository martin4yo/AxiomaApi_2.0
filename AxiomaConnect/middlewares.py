# middlewares.py
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
    
import logging
from datetime import datetime
import json
import os

# Configurar el logger para usar el nombre dinámico del archivo
logger = logging.getLogger(__name__)

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obtener los headers de la petición
        headers = {key: value for key, value in request.META.items() if key.startswith('HTTP_')}

        # Intentar obtener el body de la petición (solo si es JSON, para evitar problemas con grandes cantidades de datos o cuerpos no JSON)
        try:
            body = json.loads(request.body) if request.body else {}
        except json.JSONDecodeError:
            body = request.body.decode('utf-8')  # Si no es JSON, se guarda como texto

        # Configuración del archivo de log según la fecha actual
        log_filename = os.path.join('logs', f"{datetime.now().strftime('%Y%m%d')}.log")
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        # Loguear la solicitud completa
        logger.info(f"{datetime.now()} - {request.method} {request.path} - IP: {request.META.get('REMOTE_ADDR')}")
        logger.info(f"Headers: {headers}")
        logger.info(f"Body: {body}")

        # Llamar a la siguiente parte del middleware o vista
        response = self.get_response(request)

        # Eliminar el handler después de que se haya registrado
        logger.removeHandler(file_handler)

        return response
