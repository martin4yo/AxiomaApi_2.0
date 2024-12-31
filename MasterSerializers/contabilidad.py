from rest_framework import serializers

### CONTABLE ###############################################################

from MasterModels.contabilidad import TipoAjuste, PlanCuentas

class TipoaAjusteSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoAjuste
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PlanCuentasSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = PlanCuentas
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')
