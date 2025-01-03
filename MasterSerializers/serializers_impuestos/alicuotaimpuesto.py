from rest_framework import serializers
from MasterModels.modelos_impuestos import AlicuotaImpuesto

class AlicuotaImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = AlicuotaImpuesto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


