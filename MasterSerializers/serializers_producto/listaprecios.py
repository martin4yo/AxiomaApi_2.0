from rest_framework import serializers

from MasterModels.modelos_producto import ListaTipo
from MasterModels.modelos_producto import ListaPrecios

#from MasterSerializers.serializers_producto import ListaTipoSerializer

class ListaPreciosSerializer(serializers.ModelSerializer):
    
    """ Serializadores """
    # idtipolista = serializers.PrimaryKeyRelatedField(
    #     queryset=ListaTipo.objects.all(),
    #     write_only=True
    # )
    # idtipolista_detail = ListaTipoSerializer(source='idtipolista', read_only=True)
    
    class Meta:
        """ Clase """
        model = ListaPrecios
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')