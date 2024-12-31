from rest_framework import serializers
from MasterModels.general import Sector, FormaPago, FormaPagoDetalle, Mascara, Modulo, Rol, Persona, PersonaRol, Pais, Provincia, Partido, CodigoPostal

### Generales ######################################################

class SectorSerializer(serializers.ModelSerializer):
    """ Serializador """

    class Meta:
        """ Clase """
        model = Sector
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

### Generales ######################################################

class FormaPagoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = FormaPago
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class FormaPagoDetalleSerializer(serializers.ModelSerializer):
    """ Serializador """

    idformapago = serializers.PrimaryKeyRelatedField(
        queryset=FormaPago.objects.all(),
        write_only=True
    )

    idformapago_detail = FormaPagoSerializer(source='idformapago', read_only=True)

    class Meta:
        """ Clase """
        model = FormaPagoDetalle
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idformapago': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class MascaraSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Mascara
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ModuloSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Modulo
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class RolSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Rol
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PersonaSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Persona
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

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

class PaisSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Pais
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ProvinciaSerializer(serializers.ModelSerializer):
    """ Serializador """
    idpais = serializers.PrimaryKeyRelatedField(
        queryset=Pais.objects.all(),
        write_only=True
    )
    idpais_detail = PaisSerializer(source='idpais', read_only=True)

    class Meta:
        """ Clase """
        model = Provincia
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idpais': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class PartidoSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idprovincia = serializers.PrimaryKeyRelatedField(
        queryset=Provincia.objects.all(),
        write_only=True
    )
    idprovincia_detail = ProvinciaSerializer(source='idprovincia', read_only=True)


    class Meta:
        """ Clase """
        model = Partido
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idprovincia': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class CodigoPostalSerializer(serializers.ModelSerializer):
    """ Serializadores """
    idprovincia = serializers.PrimaryKeyRelatedField(
        queryset=Provincia.objects.all(),
        write_only=True
    )
    idprovincia_detail = ProvinciaSerializer(source='idprovincia', read_only=True)

    idpartido = serializers.PrimaryKeyRelatedField(
        queryset=Partido.objects.all(),
        write_only=True
    )
    idpartido_detail = PartidoSerializer(source='idpartido', read_only=True)

    class Meta:
        """ Clase """
        model = CodigoPostal
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idprovincia': {'write_only': True},  # Asegura que se use en el POST
            'idpartido': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')