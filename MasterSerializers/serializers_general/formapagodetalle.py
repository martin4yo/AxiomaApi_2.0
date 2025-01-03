from rest_framework import serializers
from MasterModels.modelos_general.formapago import FormaPago
from MasterModels.modelos_general.formapagodetalle import FormaPagoDetalle
from .formapago import FormaPagoSerializer

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