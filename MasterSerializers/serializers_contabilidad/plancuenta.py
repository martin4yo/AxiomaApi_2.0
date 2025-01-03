from rest_framework import serializers
from MasterModels.modelos_contabilidad.plancuentas import PlanCuentas

class PlanCuentasSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = PlanCuentas
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')
