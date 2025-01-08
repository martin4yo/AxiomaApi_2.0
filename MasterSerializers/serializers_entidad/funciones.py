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

# Funcion generica para insertar las tablas asociadas
def insert_tabla_asociada(self, entidad, model_class, data_list, unique_fields=None):
    """
    Inserta o actualiza registros en una tabla asociada.

    :param entidad: Instancia de la entidad principal.
    :param model_class: Modelo asociado (por ejemplo, ModuloEntidad).
    :param data_list: Lista de datos para insertar o actualizar.
    :param unique_fields: Lista de campos que determinan la unicidad (por defecto, usa todos los campos).
    :return: None
    """
    model_class.objects.filter(identidad=entidad).delete()
    
    # Crear nuevos registros 
    for data in data_list:
        if 'identidad' in data:
             del data['identidad']
        # data['identidad'] = entidad
        model_class.objects.create(identidad=entidad, user_id = entidad.user_id, tenant_id = entidad.tenant_id, **data)
        #model_class.objects.create(**data)

   

# def insert_tabla_asociada(self, entidad, model_class, data_list, unique_fields=None):
#     """
#     Inserta o actualiza registros en una tabla asociada.

#     :param entidad: Instancia de la entidad principal.
#     :param model_class: Modelo asociado (por ejemplo, ModuloEntidad).
#     :param data_list: Lista de datos para insertar o actualizar.
#     :param unique_fields: Lista de campos que determinan la unicidad (por defecto, usa todos los campos).
#     :return: None
#     """
#     if not data_list:
#         # Elimina todos los registros si no se proporcionan nuevos datos
#         model_class.objects.filter(identidad=entidad).delete()
#         return

#     print(data_list)

#     unique_fields = unique_fields or []
#     existing_records = model_class.objects.filter(identidad=entidad)
#     existing_tuples = set(
#         tuple(getattr(record, field) for field in unique_fields)
#         for record in existing_records
#     )

#     # Crear nuevos registros si no existen
#     for data in data_list:
#         unique_tuple = tuple(data[field] for field in unique_fields)
#         print(unique_tuple)
#         print(existing_tuples)
#         if unique_tuple not in existing_tuples:
#             # Asegúrate de que 'identidad' no esté en los datos
#             print('No es unico')
#             if 'identidad' in data:
#                 del data['identidad']
#             model_class.objects.create(identidad=entidad, **data)

#     # Eliminar registros que ya no están en la lista de datos
#     new_tuples = set(tuple(data[field] for field in unique_fields) for data in data_list)
#     for record in existing_records:
#         unique_tuple = tuple(getattr(record, field) for field in unique_fields)
#         if unique_tuple not in new_tuples:
#             record.delete()