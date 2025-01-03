from rest_framework import serializers
from .funciones import entidad_to_dict 

from MasterModels.modelos_general import Persona, Rol
from MasterModels.modelos_entidad import Entidad, EjecutivoEntidad

from MasterSerializers.serializers_general import PersonaSerializer, RolSerializer

class EjecutivoEntidadSerializer(serializers.ModelSerializer):
    """ Serializador """

    identidad = serializers.PrimaryKeyRelatedField(
        queryset=Entidad.objects.all(),
        required=False,
        allow_null=True,
        write_only=True
    )
    identidad_detail = serializers.SerializerMethodField()
    
    idpersona = serializers.PrimaryKeyRelatedField(
        queryset=Persona.objects.all(),
        write_only=True
    )
    idpersona_detail = PersonaSerializer(source='idpersona', read_only=True)

    idrol = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(),
        write_only=True
    )
    idrol_detail = RolSerializer(source='idrol', read_only=True)

    class Meta:
        """ Clase """
        model = EjecutivoEntidad
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idpersona': {'write_only': True},  # Asegura que se use en el POST
            'idrol': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')
    
    def get_identidad_detail(self, obj):
        """
        Retorna los detalles de la entidad asociada.
        """
        return entidad_to_dict(obj.identidad)

