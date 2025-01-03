from rest_framework import serializers
from MasterModels.modelos_general import Moneda, TipoFrecuencia, TipoValor, TipoIndice

from MasterSerializers.serializers_general.moneda import MonedaSerializer
from MasterSerializers.serializers_general.tipofrecuencia import TipoFrecuenciaSerializer
from MasterSerializers.serializers_general.tipovalor import  TipoValorSerializer


class TipoIndiceSerializer(serializers.ModelSerializer):
    """ Serializador """

    idmoneda = serializers.PrimaryKeyRelatedField(
        queryset=Moneda.objects.all(),
        write_only=True
    )
    idmoneda_detail = MonedaSerializer(source='idmoneda', read_only=True)

    idtipofrecuencia = serializers.PrimaryKeyRelatedField(
        queryset=TipoFrecuencia.objects.all(),
        write_only=True
    )
    idtipofrecuencia_detail = TipoFrecuenciaSerializer(source='idtipofrecuencia', read_only=True)

    idtipovalor = serializers.PrimaryKeyRelatedField(
        queryset=TipoValor.objects.all(),
        write_only=True
    )
    idtipovalor_detail = TipoValorSerializer(source='idtipovalor', read_only=True)

    class Meta:
        """ Clase """
        model = TipoIndice
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmoneda': {'write_only': True},  # Asegura que se use en el POST
            'idtipofrecuencia': {'write_only': True},  # Asegura que se use en el POST
            'idtipovalor': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')
