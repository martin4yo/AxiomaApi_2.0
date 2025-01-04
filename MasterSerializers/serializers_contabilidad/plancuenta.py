from rest_framework import serializers
from MasterModels.modelos_contabilidad.plancuenta import PlanCuenta

class PlanCuentaSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = PlanCuenta
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')
