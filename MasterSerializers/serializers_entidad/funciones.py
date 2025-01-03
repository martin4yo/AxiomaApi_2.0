# Funcion para devolver la lista de campos de Entidad

def entidad_to_dict(entidad):
    """
    Convierte una instancia de Entidad en un diccionario.
    """
    return {
        'id': entidad.id,
        'nombre': entidad.nombre,  # Ajusta según los campos que tengas en Entidad
        'nombrefantasia': entidad.nombrefantasia,  # Ajusta según los campos que tengas en Entidad
        'codigo': entidad.codigo,  # Ajusta según los campos que tengas en Entidad
        'intercompany': entidad.intercompany,  # Ajusta según los campos que tengas en Entidad
        
    }