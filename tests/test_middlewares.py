from django.test import TestCase, RequestFactory
from django.http import JsonResponse
from django.contrib.auth.models import User
from AxiomaConnect.middlewares import TenantValidationMiddleware, DynamicCORSHeadersMiddleware
import json


class TenantValidationMiddlewareTest(TestCase):
    """Tests para TenantValidationMiddleware"""
    
    def setUp(self):
        self.factory = RequestFactory()
        self.get_response = lambda request: JsonResponse({'status': 'ok'})
        self.middleware = TenantValidationMiddleware(self.get_response)
    
    def test_excluded_paths_bypass_validation(self):
        """Test que rutas excluidas pasan sin validación"""
        request = self.factory.post('/admin/login/')
        response = self.middleware(request)
        
        # Admin debe pasar sin validación
        self.assertEqual(response.status_code, 200)
    
    def test_api_token_bypasses_validation(self):
        """Test que /api/token/ pasa sin validación"""
        request = self.factory.post('/api/token/')
        response = self.middleware(request)
        
        self.assertEqual(response.status_code, 200)
    
    def test_get_requests_bypass_validation(self):
        """Test que requests GET pasan sin validación"""
        request = self.factory.get('/api/personas/')
        response = self.middleware(request)
        
        self.assertEqual(response.status_code, 200)
    
    def test_post_without_tenant_id_rejected(self):
        """Test que POST sin tenant_id es rechazado"""
        request = self.factory.post(
            '/api/personas/',
            data=json.dumps({'nombre': 'Juan'}),
            content_type='application/json'
        )
        response = self.middleware(request)
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn('tenant_id', data['error'])
    
    def test_post_with_valid_tenant_id_accepted(self):
        """Test que POST con tenant_id válido es aceptado"""
        request = self.factory.post(
            '/api/personas/',
            data=json.dumps({
                'nombre': 'Juan',
                'tenant_id': 1
            }),
            content_type='application/json'
        )
        response = self.middleware(request)
        
        # Debe pasar la validación y continuar
        self.assertEqual(response.status_code, 200)
        self.assertEqual(request.tenant_id, 1)
    
    def test_post_with_invalid_tenant_id_rejected(self):
        """Test que POST con tenant_id inválido es rechazado"""
        request = self.factory.post(
            '/api/personas/',
            data=json.dumps({
                'nombre': 'Juan',
                'tenant_id': 0
            }),
            content_type='application/json'
        )
        response = self.middleware(request)
        
        self.assertEqual(response.status_code, 403)
        data = json.loads(response.content)
        self.assertIn('tenant_id', data['error'])
    
    def test_tenant_id_from_header(self):
        """Test extracción de tenant_id desde header"""
        request = self.factory.post(
            '/api/personas/',
            data=json.dumps({'nombre': 'Juan'}),
            content_type='application/json',
            HTTP_X_TENANT_ID='1'
        )
        response = self.middleware(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(request.tenant_id, 1)


class DynamicCORSHeadersMiddlewareTest(TestCase):
    """Tests para DynamicCORSHeadersMiddleware"""
    
    def setUp(self):
        self.factory = RequestFactory()
        self.get_response = lambda request: JsonResponse({'status': 'ok'})
        self.middleware = DynamicCORSHeadersMiddleware()
    
    def test_localhost_origin_allowed(self):
        """Test que localhost es permitido con CORS"""
        request = self.factory.get('/', HTTP_ORIGIN='http://localhost:3000')
        response = JsonResponse({'status': 'ok'})
        
        response = self.middleware.process_response(request, response)
        
        self.assertEqual(
            response['Access-Control-Allow-Origin'], 
            'http://localhost:3000'
        )
        self.assertEqual(
            response['Access-Control-Allow-Credentials'], 
            'true'
        )
    
    def test_non_localhost_origin_not_modified(self):
        """Test que orígenes no localhost no modifican headers"""
        request = self.factory.get('/', HTTP_ORIGIN='http://malicious.com')
        response = JsonResponse({'status': 'ok'})
        
        response = self.middleware.process_response(request, response)
        
        # No debe agregar headers CORS
        self.assertNotIn('Access-Control-Allow-Origin', response)
    
    def test_no_origin_header_not_modified(self):
        """Test que requests sin Origin no modifican headers"""
        request = self.factory.get('/')
        response = JsonResponse({'status': 'ok'})
        
        response = self.middleware.process_response(request, response)
        
        # No debe agregar headers CORS
        self.assertNotIn('Access-Control-Allow-Origin', response)