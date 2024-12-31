from rest_framework import serializers
from django.db import transaction

from MasterSerializers.entidad_tablas import ModuloEntidadSerializer, CondicionCrediticiaEntidadSerializer, ImpuestoEntidadSerializer
from MasterSerializers.entidad_tablas import EjecutivoEntidadSerializer, DatosFiscalesEntidadSerializer, ContactoEntidadSerializer
from MasterSerializers.entidad_tablas import DireccionEntidadSerializer, SectorEntidadSerializer, FormaPagoEntidadSerializer
from MasterSerializers.impuestos import TipoResponsableSerializer 

from MasterModels.entidad import Entidad, ModuloEntidad, CondicionCrediticiaEntidad, ImpuestoEntidad
from MasterModels.entidad import EjecutivoEntidad, ContactoEntidad, SectorEntidad, DatosFiscalesEntidad, DireccionEntidad, FormaPagoEntidad

from MasterModels.general import TipoResponsable

class EntidadSerializer(serializers.ModelSerializer):
    """ Serializador """
    entidad_modulo = ModuloEntidadSerializer(many=True, required=False)  # Anidar el serializador
    entidad_condicioncrediticia = CondicionCrediticiaEntidadSerializer(many=True, required=False)  # Anidar el serializador
    entidad_impuesto = ImpuestoEntidadSerializer(many=True, required=False)  # Anidar el serializador
    entidad_ejecutivo = EjecutivoEntidadSerializer(many=True, required=False)  # Anidar el serializador
    entidad_datosfiscales = DatosFiscalesEntidadSerializer(many=True, required=False)  # Anidar el serializador
    entidad_contacto = ContactoEntidadSerializer(many=True, required=False)  # Anidar el serializador
    entidad_direccion = DireccionEntidadSerializer(many=True, required=False)  # Anidar el serializador
    entidad_sector = SectorEntidadSerializer(many=True, required=False)  # Anidar el serializador
    entidad_formapago = FormaPagoEntidadSerializer(many=True, required=False)

    idtiporesponsable = serializers.PrimaryKeyRelatedField(
        queryset=TipoResponsable.objects.all(),
        required=False,
        allow_null=True,
        write_only=True
    )
    idtiporesponsable_detail = TipoResponsableSerializer(source='idtiporesponsable', read_only=True, required=False)

    class Meta:
        """ Clase """
        model = Entidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idtiporesponsable': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

    # Creacion de la entidad

    def create(self, validated_data):
        try:
            entidad_modulo = validated_data.pop('entidad_modulo', [])
            entidad_condicioncrediticia = validated_data.pop('entidad_condicioncrediticia', [])
            entidad_impuesto = validated_data.pop('entidad_impuesto', [])
            entidad_ejecutivo = validated_data.pop('entidad_ejecutivo', [])
            entidad_datosfiscales = validated_data.pop('entidad_datosfiscales', [])
            entidad_contacto = validated_data.pop('entidad_contacto', [])
            entidad_direccion = validated_data.pop('entidad_direccion', [])
            entidad_sector = validated_data.pop('entidad_sector', [])
            entidad_formapago = validated_data.pop('entidad_formapago', [])

            with transaction.atomic():

                entidad = Entidad.objects.create(**validated_data)
            
                # Crear registros en ModulosPorEntidad
                for modulo_data in entidad_modulo:       
                    ModuloEntidad.objects.create(
                        identidad=entidad, 
                        idmodulo=modulo_data['idmodulo'],
                        user_id=entidad.user_id,
                        tenant_id=entidad.tenant_id
                        )
            
                # Crear registros en CondicionCrediticiaEntidad
                for condicioncrediticia_data in entidad_condicioncrediticia:       
                    CondicionCrediticiaEntidad.objects.create(
                        identidad=entidad, 
                        idmodulo=condicioncrediticia_data['idmodulo'],
                        vigenciadesde=condicioncrediticia_data['vigenciadesde'],
                        vigenciahasta=condicioncrediticia_data['vigenciahasta'],
                        limitedesde=condicioncrediticia_data['limitedesde'],
                        limitehasta=condicioncrediticia_data['limitehasta'],
                        user_id=entidad.user_id,
                        tenant_id=entidad.tenant_id
                        )
            
                # Crear registros en ImpuestoPorEntidad
                for impuesto_data in entidad_impuesto:       
                    ImpuestoEntidad.objects.create(
                        identidad=entidad, 
                        idmodulo=impuesto_data['idmodulo'],
                        idimpuesto=impuesto_data['idimpuesto'],
                        aplica=impuesto_data['aplica'],
                        user_id=entidad.user_id,
                        tenant_id=entidad.tenant_id
                        )
            
                # Crear registros en EjecutivoPorEntidad
                for ejecutivo_data in entidad_ejecutivo:       
                    EjecutivoEntidad.objects.create(
                        identidad=entidad, 
                        idpersona=ejecutivo_data['idpersona'],
                        idrol=ejecutivo_data['idrol'],
                        user_id=entidad.user_id,
                        tenant_id=entidad.tenant_id
                        )
            
                # Crear registros en DatosFiscalesEntidad
                for datosfiscales_data in entidad_datosfiscales:       
                    DatosFiscalesEntidad.objects.create(
                        identidad=entidad, 
                        idtipodocumento=datosfiscales_data['idtipodocumento'],
                        idtiposujeto=datosfiscales_data['idtiposujeto'],
                        numerodocumento=datosfiscales_data['numerodocumento'],
                        user_id=entidad.user_id,
                        tenant_id=entidad.tenant_id
                        )
            
                # Crear registros en ContactoEntidad
                for contacto_data in entidad_contacto:       
                    ContactoEntidad.objects.create(
                        identidad=entidad, 
                        nombre=contacto_data['nombre'],
                        rol=contacto_data['rol'],
                        telefono=contacto_data['telefono'],
                        sector=contacto_data['sector'],
                        user_id=entidad.user_id,
                        tenant_id=entidad.tenant_id
                        )
            
                # Crear registros en DireccionEntidad
                for direccion_data in entidad_direccion:       
                    DireccionEntidad.objects.create(
                        identidad=entidad, 
                        nombre=direccion_data['nombre'],
                        idtiposede=direccion_data['idtiposede'],
                        idtipodomicilio=direccion_data['idtipodomicilio'],
                        calle=direccion_data['calle'],
                        numero=direccion_data['numero'],
                        piso=direccion_data['piso'],
                        departamento=direccion_data['departamento'],
                        idpais=direccion_data['idpais'],
                        idprovincia=direccion_data['idprovincia'],
                        idpartido=direccion_data['idpartido'],
                        idcodigopostal=direccion_data['idcodigopostal'],
                        idzona=direccion_data['idzona'],
                        diasentrega=direccion_data['diasentrega'],
                        diasretiro=direccion_data['diasretiro'],
                        user_id=entidad.user_id,
                        tenant_id=entidad.tenant_id
                        )
                   
                # Crear registros en SectorEntidad
                for sector_data in entidad_sector:       
                    SectorEntidad.objects.create(
                        identidad=entidad, 
                        idmodulo=sector_data['idmodulo'],
                        idsector=sector_data['idsector'],
                        user_id=entidad.user_id,
                        tenant_id=entidad.tenant_id
                        )
            
                # Crear registros en FormaPagoEntidad
                for formapago_data in entidad_formapago:       
                    FormaPagoEntidad.objects.create(
                        identidad=entidad, 
                        idmodulo=sector_data['idmodulo'],
                        idformapago=formapago_data['idformapago'],
                        user_id=entidad.user_id,
                        tenant_id=entidad.tenant_id
                        )

            return entidad
        
        except serializers.ValidationError as e:
            print(f"Validation errors: {e}")
            raise

    # Update de la entidad
    # 
    # def update(self, instance, validated_data):
    #     modulos_data = validated_data.pop('modulos', [])
    #     instance.nombre = validated_data.get('nombre', instance.nombre)
    #     instance.save()

    #     # Actualizar registros en ModulosPorEntidad
    #     modulo_ids = [modulo_data['modulo_id'] for modulo_data in modulos_data]

    #     # Eliminar módulos que ya no están en la lista
    #     ModulosPorEntidad.objects.filter(entidad=instance).exclude(modulo_id__in=modulo_ids).delete()

    #     # Agregar los nuevos módulos
    #     existing_modulo_ids = ModulosPorEntidad.objects.filter(entidad=instance).values_list('modulo_id', flat=True)
    #     for modulo_id in modulo_ids:
    #         if modulo_id not in existing_modulo_ids:
    #             ModulosPorEntidad.objects.create(entidad=instance, modulo_id=modulo_id)

    #     return instance    

    # def validate(self, attrs):
    #     request = self.context.get('request')  # Obtenemos el tipo de solicitud
    #     if request and request.method == 'POST':
    #         # En POST, aseguramos que 'nombre' esté presente y no sea vacío
    #         if 'codigo' not in attrs or not attrs['codigo'].strip():
    #             raise serializers.ValidationError({
    #                 'codigo': 'Este campo es obligatorio para crear una entidad.'
    #             })
    #         # En POST, aseguramos que 'nombre' esté presente y no sea vacío
    #         if 'idtiporesponsable' not in attrs or not attrs['idtiporesponsable'].strip():
    #             raise serializers.ValidationError({
    #                 'idtiporesponsable': 'Este campo es obligatorio para crear una entidad.'
    #             })
    #     return attrs
    
