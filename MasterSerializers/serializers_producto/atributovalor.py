from rest_framework import serializers
from MasterModels.modelos_producto.atributovalor import AtributoValor
from MasterModels.modelos_producto.atributo import Atributo

from MasterSerializers.serializers_producto.atributo import AtributoSerializer

class AtributoValorSerializer(serializers.ModelSerializer):

    idatributo = serializers.PrimaryKeyRelatedField(
        queryset=Atributo.objects.all(),
        write_only=True
    )
    idatributo_detail = AtributoSerializer(source='idatributo', read_only=True)

    """ Serializador """
    class Meta:
        """ Clase """
        model = AtributoValor
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


