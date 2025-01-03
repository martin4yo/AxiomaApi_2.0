from rest_framework import serializers
from MasterModels.modelos_impuestos import TipoImpuesto, AlicuotaImpuesto, PadronImpuesto, Impuesto
from MasterModels.modelos_general import Provincia, Partido
from MasterModels.modelos_contabilidad import PlanCuentas 

from MasterSerializers.serializers_general import ProvinciaSerializer, PartidoSerializer
from MasterSerializers.serializers_impuestos.tipoimpuesto import TipoImpuestoSerializer
from MasterSerializers.serializers_impuestos.alicuotaimpuesto import AlicuotaImpuestoSerializer
from MasterSerializers.serializers_impuestos.padronimpuesto import PadronImpuestoSerializer
from MasterSerializers.serializers_contabilidad import PlanCuentasSerializer 

class ImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """

    idtipoimpuesto = serializers.PrimaryKeyRelatedField(
        queryset=TipoImpuesto.objects.all(),
        write_only=True
    )
    idtipoimpuesto_detail = TipoImpuestoSerializer(source='idclasificacionimpuesto', read_only=True)

    idalicuota = serializers.PrimaryKeyRelatedField(
        queryset=AlicuotaImpuesto.objects.all(),
        write_only=True
    )
    idalicuota_detail = AlicuotaImpuestoSerializer(source='idalicuota', read_only=True)

    idplancuenta = serializers.PrimaryKeyRelatedField(
        queryset = PlanCuentas.objects.all(),
        write_only=True
    )
    idplancuenta_detail = PlanCuentasSerializer(source='idplancuenta', read_only=True)

    idpadron = serializers.PrimaryKeyRelatedField(
        queryset=PadronImpuesto.objects.all(),
        write_only=True
    )
    idpadron_detail = PadronImpuestoSerializer(source='idpadron', read_only=True)

    idprovincia = serializers.PrimaryKeyRelatedField(
        queryset=Provincia.objects.all(),
        write_only=True
    )
    idprovincia_detail = ProvinciaSerializer(source='idprovincia', read_only=True)

    idpartido = serializers.PrimaryKeyRelatedField(
        queryset=Partido.objects.all(),
        write_only=True
    )
    idpartido_detail = PartidoSerializer(source='idpartido', read_only=True)

    class Meta:
        """ Clase """
        model = Impuesto   
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idimpuesto': {'write_only': True},  # Asegura que se use en el POST
            'idalicuota': {'write_only': True},  # Asegura que se use en el POST
            'idplancuenta': {'write_only': True},  # Asegura que se use en el POST
            'idpadron': {'write_only': True},  # Asegura que se use en el POST
            'idprovincia': {'write_only': True},  # Asegura que se use en el POST
            'idpartido': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')
