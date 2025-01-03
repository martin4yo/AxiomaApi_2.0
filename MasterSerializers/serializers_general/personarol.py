from rest_framework import serializers
from MasterModels.modelos_general.persona import Persona
from MasterModels.modelos_general.rol import Rol
from MasterModels.modelos_general.personarol import PersonaRol

from .persona import PersonaSerializer
from .rol import RolSerializer

class PersonaRolSerializer(serializers.ModelSerializer):
    """ Serializador """

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
        model = PersonaRol
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idpersona': {'write_only': True},  # Asegura que se use en el POST
            'idrol': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')
