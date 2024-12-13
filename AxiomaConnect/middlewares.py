# middlewares.py
class AddCOOPHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        origin = request.headers.get("Origin")
        # Agregar el encabezado COOP
        response['Cross-Origin-Opener-Policy'] = 'unsafe-none'  # Puedes cambiar a 'unsafe-none' si es necesario
        response["Access-Control-Allow-Origin"] = origin
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Authorization, Content-Type, X-CSRFToken"
        return response
    

import re 
from django.utils.deprecation import MiddlewareMixin

class DynamicCORSHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        origin = request.headers.get("Origin")
        allowed_pattern = re.compile(r"^http?://(\w+\.)?axiomacloud\.com$")
        
        if origin and allowed_pattern.match(origin):
            response["Access-Control-Allow-Origin"] = origin
            response["Access-Control-Allow-Credentials"] = "true"
            response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Authorization, Content-Type, X-CSRFToken"

        return response