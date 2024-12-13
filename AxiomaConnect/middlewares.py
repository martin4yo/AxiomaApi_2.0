# middlewares.py
class AddCOOPHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Agregar el encabezado COOP
        response['Cross-Origin-Opener-Policy'] = 'unsafe-none'  # Puedes cambiar a 'unsafe-none' si es necesario
        return response