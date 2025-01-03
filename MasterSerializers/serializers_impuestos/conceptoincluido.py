from rest_framework import serializers
from MasterModels.modelos_impuestos import ConceptoIncluido

class ConceptoIncluidoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = ConceptoIncluido
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')
