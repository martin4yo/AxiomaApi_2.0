from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from MasterModels.universal import TenantModel, AuditModel, ValidatedModel
from MasterModels.modelos_general.persona import Persona
from django.db import models


class TenantModelTest(TestCase):
    """Tests para TenantModel"""
    
    def test_tenant_id_positive_validation(self):
        """Test que tenant_id debe ser positivo"""
        
        # Crear una clase concreta para testing
        class TestTenantModel(TenantModel):
            class Meta:
                app_label = 'tests'
        
        # Test con tenant_id válido
        instance = TestTenantModel(tenant_id=1)
        try:
            instance.clean()
        except ValidationError:
            self.fail("clean() raised ValidationError unexpectedly with valid tenant_id")
        
        # Test con tenant_id inválido (0)
        instance = TestTenantModel(tenant_id=0)
        with self.assertRaises(ValidationError):
            instance.clean()
        
        # Test con tenant_id inválido (negativo)
        instance = TestTenantModel(tenant_id=-1)
        with self.assertRaises(ValidationError):
            instance.clean()
    
    def test_tenant_id_can_be_null(self):
        """Test que tenant_id puede ser nulo"""
        
        class TestTenantModel(TenantModel):
            class Meta:
                app_label = 'tests'
        
        instance = TestTenantModel(tenant_id=None)
        try:
            instance.clean()
        except ValidationError:
            self.fail("clean() raised ValidationError unexpectedly with null tenant_id")


class ValidatedModelTest(TestCase):
    """Tests para ValidatedModel"""
    
    def setUp(self):
        """Configurar datos de prueba"""
        self.user = User.objects.create_user(username='testuser')
        
        # Crear persona con campos reales del modelo
        self.persona = Persona.objects.create(
            nombre='TestUser',
            direccion='Test Address',
            telefono='123456789',
            usuario=self.user,
            mail='test@test.com',
            password='testpass'
        )
    
    def test_validate_unique_per_tenant(self):
        """Test validación de unicidad por tenant"""
        
        # Crear una clase de prueba que usa ValidatedModel y TenantModel
        class TestModel(ValidatedModel, TenantModel):
            nombre = models.CharField(max_length=100)
            
            class Meta:
                app_label = 'tests'
        
        # Test que la validación funciona
        instance = TestModel(nombre='test', tenant_id=1)
        try:
            instance.validate_unique_per_tenant('nombre')
        except ValidationError:
            self.fail("validate_unique_per_tenant raised ValidationError unexpectedly")


class AuditModelTest(TestCase):
    """Tests para AuditModel"""
    
    def test_audit_fields_auto_populated(self):
        """Test que los campos de auditoría se llenan automáticamente"""
        
        user = User.objects.create_user(username='testuser2')
        persona = Persona.objects.create(
            nombre='TestUser2',
            direccion='Test Address 2',
            telefono='987654321',
            usuario=user,
            mail='test2@test.com',
            password='testpass2'
        )
        
        # Verificar que created_at y updated_at se establecen
        self.assertIsNotNone(persona.created_at)
        self.assertIsNotNone(persona.updated_at)
        
        # Verificar que disabled es False por defecto
        self.assertFalse(persona.disabled)