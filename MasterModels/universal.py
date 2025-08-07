# Clase general de auditoria #######################################################

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class AuditModel(models.Model):
    """ Clase abstracta de auditoria para todas las clases """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)
    user_id = models.ForeignKey('Persona', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        """ Seteo de clase abstracta """
        abstract = True

class TenantModel(models.Model):
    tenant_id = models.BigIntegerField(
        blank=True, 
        null=True,
        validators=[MinValueValidator(1)],
        help_text="ID del inquilino (tenant)"
    )

    class Meta:
        abstract = True
    
    def clean(self):
        """Validaciones adicionales del modelo"""
        super().clean()
        if self.tenant_id is not None and self.tenant_id <= 0:
            raise ValidationError('El tenant_id debe ser un número positivo')
    
    def save(self, *args, **kwargs):
        """Ejecutar clean antes de guardar"""
        self.full_clean()
        super().save(*args, **kwargs)


class ValidatedModel(models.Model):
    """Modelo base que incluye validaciones comunes"""
    
    class Meta:
        abstract = True
    
    def validate_unique_per_tenant(self, field_name):
        """Valida que un campo sea único por tenant"""
        if hasattr(self, 'tenant_id') and self.tenant_id:
            field_value = getattr(self, field_name)
            if field_value:
                existing = self.__class__.objects.filter(
                    tenant_id=self.tenant_id,
                    **{field_name: field_value}
                ).exclude(pk=self.pk)
                
                if existing.exists():
                    raise ValidationError(
                        f'Ya existe un registro con este {field_name} para el tenant actual'
                    )

from django.apps import apps

def listar_tablas_modelos():
    modelos = apps.get_models()
    return [model._meta.db_table for model in modelos]