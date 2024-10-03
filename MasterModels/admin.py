""" admin """
from django.contrib import admin
from django.apps import apps

# Register your models here.

# class PersonaAdmin(admin.ModelAdmin):
#     """ Todas las columnas"""
#     list_display = [field.name for field in Persona._meta.fields]

# class TipoDocumentoAdmin(admin.ModelAdmin):
#     """ Todas las columnas"""
#     list_display = [field.name for field in TipoDocumento._meta.fields]

# 
# admin.site.register(Persona, PersonaAdmin)
# admin.site.register(TipoDocumento, TipoDocumentoAdmin)
# 

# Lista de tus aplicaciones, definidas en INSTALLED_APPS
my_apps =   [
            'MasterModels', 
            ]  # Reemplaza con los nombres de tus aplicaciones

# Itera sobre las aplicaciones que has creado
for app_label in my_apps:
    app_config = apps.get_app_config(app_label)
    models = app_config.get_models()

    # Itera sobre los modelos de la aplicación y regístralos en el admin
    for model in models:
        try:
            
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            # Ya está registrado, omitir
            pass