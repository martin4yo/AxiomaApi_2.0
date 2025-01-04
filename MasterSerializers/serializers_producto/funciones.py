# Funcion para devolver la lista de campos de Entidad

def producto_to_dict(producto):
    """
    Convierte una instancia de Producto en un diccionario.
    """
    return {
        'id': producto.id,
        'idtipoproducto': producto.idtipoproducto.codigo,  # Ajusta según los campos que tengas en Entidad
        'codigo': producto.codigo,  # Ajusta según los campos que tengas en Entidad
        'nombre': producto.nombre,  # Ajusta según los campos que tengas en Entidad
        'unidadmedida': producto.idunidadmedida.codigo,  # Ajusta según los campos que tengas en Entidad
        'clase': producto.idclaseproducto.codigo,  # Ajusta según los campos que tengas en Entidad
    }

