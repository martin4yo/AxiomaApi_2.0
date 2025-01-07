from rest_framework import serializers
from django.db import transaction
from django.db.models import Q
from .funciones import insert_tabla_asociada

from MasterSerializers.serializers_entidad.moduloentidad import ModuloEntidadSerializer
from MasterSerializers.serializers_entidad.condicioncrediticiaentidad import CondicionCrediticiaEntidadSerializer
from MasterSerializers.serializers_entidad.impuestoentidad import ImpuestoEntidadSerializer
from MasterSerializers.serializers_entidad.ejecutivoentidad import EjecutivoEntidadSerializer
from MasterSerializers.serializers_entidad.datosfiscalesentidad import DatosFiscalesEntidadSerializer
from MasterSerializers.serializers_entidad.contactoentidad import ContactoEntidadSerializer
from MasterSerializers.serializers_entidad.direccionentidad import DireccionEntidadSerializer
from MasterSerializers.serializers_entidad.sectorentidad import SectorEntidadSerializer
from MasterSerializers.serializers_entidad.formapagoentidad import FormaPagoEntidadSerializer
from MasterSerializers.serializers_general.tiporesponsable import TipoResponsableSerializer 
from MasterSerializers.serializers_entidad.listaprecioentidad import ListaPrecioEntidadSerializer 

from MasterModels.modelos_entidad import Entidad, ModuloEntidad, CondicionCrediticiaEntidad, ImpuestoEntidad, ListaPrecioEntidad
from MasterModels.modelos_entidad import EjecutivoEntidad, ContactoEntidad, SectorEntidad, DatosFiscalesEntidad, DireccionEntidad, FormaPagoEntidad

from MasterModels.modelos_general.tiporesponsable import TipoResponsable

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
    entidad_lista = ListaPrecioEntidadSerializer(many=True, required=False)

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
            entidad_lista = validated_data.pop('entidad_lista', [])
            
            with transaction.atomic():

                entidad = Entidad.objects.create(**validated_data)

                insert_tabla_asociada(self, entidad, ModuloEntidad, entidad_modulo)
                insert_tabla_asociada(self, entidad, CondicionCrediticiaEntidad, entidad_condicioncrediticia)
                insert_tabla_asociada(self, entidad, ImpuestoEntidad, entidad_impuesto)
                insert_tabla_asociada(self, entidad, EjecutivoEntidad, entidad_ejecutivo)
                insert_tabla_asociada(self, entidad, DatosFiscalesEntidad, entidad_datosfiscales)
                insert_tabla_asociada(self, entidad, ContactoEntidad, entidad_contacto)
                insert_tabla_asociada(self, entidad, DireccionEntidad, entidad_direccion)
                insert_tabla_asociada(self, entidad, SectorEntidad, entidad_sector)
                insert_tabla_asociada(self, entidad, FormaPagoEntidad, entidad_formapago)
                insert_tabla_asociada(self, entidad, ListaPrecioEntidad, entidad_lista)

            return entidad
        
        except serializers.ValidationError as e:
            print(f"Validation errors: {e}")
            raise

    # Update de la entidad
    
    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.nombrefantasia = validated_data.get('nombrefantasia', instance.nombrefantasia)
        instance.codigo = validated_data.get('codigo', instance.codigo)
        instance.intercompany = validated_data.get('intercompany', instance.intercompany)
        instance.idtiporesponsable = validated_data.get('idtiporesponsable', instance.idtiporesponsable)

        instance.save()

        # Actualizar tablas asociadas ############################################################################################

        if 'entidad_modulo' in validated_data:
            insert_tabla_asociada(self, instance, ModuloEntidad, validated_data.pop('entidad_modulo', []))

        if 'entidad_condicioncrediticia' in validated_data:
            insert_tabla_asociada(self, instance, CondicionCrediticiaEntidad, validated_data.pop('entidad_condicioncrediticia', []))

        if 'entidad_impuesto' in validated_data:
            insert_tabla_asociada(self, instance, ImpuestoEntidad, validated_data.pop('entidad_impuesto', []))

        if 'entidad_ejecutivo' in validated_data:
            insert_tabla_asociada(self, instance, EjecutivoEntidad, validated_data.pop('entidad_ejecutivo', []))

        if 'entidad_datosfiscales' in validated_data:
            insert_tabla_asociada(self, instance, DatosFiscalesEntidad, validated_data.pop('entidad_datosfiscales', []))

        if 'entidad_contacto' in validated_data:
            insert_tabla_asociada(self, instance, ContactoEntidad, validated_data.pop('entidad_contacto', []))

        if 'entidad_direccion' in validated_data:
            insert_tabla_asociada(self, instance, DireccionEntidad, validated_data.pop('entidad_direccion', []))

        if 'entidad_sector' in validated_data:
            insert_tabla_asociada(self, instance, SectorEntidad, validated_data.pop('entidad_sector', []))

        if 'entidad_formapago' in validated_data:
            insert_tabla_asociada(self, instance, FormaPagoEntidad, validated_data.pop('entidad_formapago', []))
            
        if 'entidad_lista' in validated_data:
            insert_tabla_asociada(self, instance, ListaPrecioEntidad, validated_data.pop('entidad_lista', []))

        return instance    
    
    
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
    
