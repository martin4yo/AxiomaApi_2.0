from rest_framework import serializers
from MasterModels.modelos_general.moneda import Moneda
from MasterModels.modelos_general.tipocambio import TipoCambio

from MasterSerializers.serializers_general.moneda import MonedaSerializer

class TipoCambioSerializer(serializers.ModelSerializer):
    """ Serializador """

    idmoneda = serializers.PrimaryKeyRelatedField(
        queryset=Moneda.objects.all(),
        write_only=True
    )
    idmoneda_detail = MonedaSerializer(source='idmoneda', read_only=True)

    class Meta:
        """ Clase """
        model = TipoCambio
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmoneda': {'write_only': True},  # Asegura que `zona` se use en el POST
        }
        #fields = ['id', 'idmoneda','fecha','comprador']
        read_only_fields = ('created_at', 'updated_at')

