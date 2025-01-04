from rest_framework import serializers
from MasterModels.modelos_impuestos import PadronImpuesto

class PadronImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = PadronImpuesto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')