from django.apps import apps
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class TablasViewSet(ViewSet):
    def list(self, request):
        # Obtener las tablas de los modelos registrados
        modelos = apps.get_models()
        modelos = [model for model in modelos if model._meta.app_label == "MasterModels"]
        tablas = [model._meta.db_table for model in modelos]

        # Retirar el prefijo 'prefix_' de los nombres de las tablas
        prefijo = "MasterModels_"
        tablas_sin_prefijo = [tabla.removeprefix(prefijo) for tabla in tablas]
        tablas_ordenadas = sorted(tablas_sin_prefijo)

        return Response({"tablas": tablas_ordenadas})
    
class TablasConCodigoViewSet(ViewSet):
    def list(self, request):
        # Obtener las tablas de los modelos registrados
        modelos = apps.get_models()
        modelos = [model for model in modelos if model._meta.app_label == "MasterModels"]
        tablas = []

        for model in modelos:
            campos = [field.name for field in model._meta.fields]
            if "codigo" in campos:
                tablas.append(model._meta.db_table)

        # Retirar el prefijo 'prefix_' de los nombres de las tablas
        prefijo = "MasterModels_"
        tablas_sin_prefijo = [tabla.removeprefix(prefijo) for tabla in tablas]
        tablas_ordenadas = sorted(tablas_sin_prefijo)

        return Response({"tablas": tablas_ordenadas})

