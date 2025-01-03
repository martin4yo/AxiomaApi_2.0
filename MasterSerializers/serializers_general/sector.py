from rest_framework import serializers
from MasterModels.modelos_general.sector import Sector

class SectorSerializer(serializers.ModelSerializer):
    """ Serializador """

    class Meta:
        """ Clase """
        model = Sector
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')
