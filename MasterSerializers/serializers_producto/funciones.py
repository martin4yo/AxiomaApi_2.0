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

# Funcion generica para insertar las tablas asociadas
def insert_tabla_asociada(self, producto, model_class, data_list, unique_fields=None):
    """
    Inserta o actualiza registros en una tabla asociada.

    :param entidad: Instancia de la entidad principal.
    :param model_class: Modelo asociado (por ejemplo, ModuloEntidad).
    :param data_list: Lista de datos para insertar o actualizar.
    :param unique_fields: Lista de campos que determinan la unicidad (por defecto, usa todos los campos).
    :return: None
    """
    model_class.objects.filter(idproducto=producto).delete()
    
    # Crear nuevos registros 
    for data in data_list:
        if 'idproducto' in data:
             del data['idproducto']
        if 'tenant_id' in data:
             del data['tenant_id']
        if 'userid_id' in data:
             del data['userid_id']
        # data['identidad'] = entidad
        model_class.objects.create(idproducto=producto, user_id = producto.user_id, tenant_id = producto.tenant_id, **data)
        #model_class.objects.create(**data)