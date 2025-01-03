from rest_framework import serializers
from MasterModels.modelos_impuestos import ClasificacionImpuesto, TipoImpuesto

from MasterSerializers.serializers_impuestos.clasificacionimpuesto import ClasificacionImpuestoSerializer


class TipoImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """

    idclasificacionimpuesto = serializers.PrimaryKeyRelatedField(
        queryset=ClasificacionImpuesto.objects.all(),
        write_only=True
    )
    idclasificacionimpuesto_detail = ClasificacionImpuestoSerializer(source='idclasificacionimpuesto', read_only=True)

    class Meta:
        """ Clase """
        model = TipoImpuesto   
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idclasificacionimpuesto': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')