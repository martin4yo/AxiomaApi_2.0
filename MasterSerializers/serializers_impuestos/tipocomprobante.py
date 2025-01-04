from rest_framework import serializers
from MasterModels.modelos_impuestos import TipoComprobante

class TipoComprobanteSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = TipoComprobante   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')