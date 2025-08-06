from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  # Permitir acceso sin autenticación
@csrf_exempt
def validate_user(request):
    """
    Endpoint para validar credenciales de usuario
    
    GET: /api/auth/validate/?username=test&password=123
    POST: /api/auth/validate/ con JSON body
    """

    # Obtener credenciales según el método HTTP
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
    else:  # POST
        username = request.data.get('username')
        password = request.data.get('password')

    # Validar que se enviaron ambos campos
    if not username or not password:
        return Response({
            'success': False,
            'valid': False,
            'message': 'Debe ingresar usuario y contraseña',
            'error': 'MISSING_CREDENTIALS'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Verificar que el usuario existe
        user_exists = User.objects.filter(username=username).exists()
        if not user_exists:
            return Response({
                'success': False,
                'valid': False,
                'message': 'Usuario inexistente',
                'error': 'USER_NOT_FOUND'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Autenticar usuario
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Usuario válido
            if user.is_active:
                return Response({
                    'success': True,
                    'valid': True,
                    'authenticated': True,
                    'message': 'User authenticated successfully',
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'full_name': f"{user.first_name} {user.last_name}".strip(),
                        'is_staff': user.is_staff,
                        'is_superuser': user.is_superuser,
                        'is_active': user.is_active,
                        'date_joined': user.date_joined.isoformat(),
                        'last_login': user.last_login.isoformat() if user.last_login else None,
                    }
                }, status=status.HTTP_200_OK)
            else:
                # Usuario existe pero está inactivo
                return Response({
                    'success': False,
                    'valid': False,
                    'message': 'Usuario inactivo',
                    'error': 'USER_INACTIVE'
                }, status=status.HTTP_403_FORBIDDEN)
        else:
            # Credenciales incorrectas
            return Response({
                'success': False,
                'valid': False,
                'message': 'Credenciales inválidas',
                'error': 'INVALID_CREDENTIALS'
            }, status=status.HTTP_401_UNAUTHORIZED)
            
    except Exception as e:
        # Error interno del servidor
        return Response({
            'success': False,
            'valid': False,
            'message': 'Internal server error',
            'error': f'SERVER_ERROR: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)