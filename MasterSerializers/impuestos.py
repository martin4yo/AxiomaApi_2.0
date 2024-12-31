from rest_framework import serializers

### IMPOSITIVO ###############################################################

from MasterModels.general import TipoDocumento, TipoResponsable,  Incoterms, Moneda, TipoDeCambio, Mascara, Pais
from MasterModels.general import Idioma, UnidadMedida,  TipoIndice, TipoFrecuencia, TipoValor, Indice, Provincia, Partido
from MasterModels.contabilidad import PlanCuentas
from MasterModels.impuestos import TipoSujeto, ConceptoIncluido, TipoComprobante, CuitPais, AlicuotaImpuesto
from MasterModels.impuestos import PadronImpuesto, TipoCalculo,  ClasificacionImpuesto
from MasterModels.impuestos import TipoImpuesto, Impuesto

from MasterSerializers.general import MascaraSerializer, ProvinciaSerializer, PartidoSerializer
from MasterSerializers.contabilidad import PlanCuentasSerializer, TipoaAjusteSerializer

class TipoCalculoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = TipoCalculo   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class MonedaSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Moneda   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoDeCambioSerializer(serializers.ModelSerializer):
    """ Serializador """

    idmoneda = serializers.PrimaryKeyRelatedField(
        queryset=Moneda.objects.all(),
        write_only=True
    )
    idmoneda_detail = MonedaSerializer(source='idmoneda', read_only=True)

    class Meta:
        """ Clase """
        model = TipoDeCambio
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmoneda': {'write_only': True},  # Asegura que `zona` se use en el POST
        }
        #fields = ['id', 'idmoneda','fecha','comprador']
        read_only_fields = ('created_at', 'updated_at')


class TipoComprobanteSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = TipoComprobante   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class UnidadMedidaSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = UnidadMedida   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class IdiomaSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Idioma   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class IncotermsSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = Incoterms   
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ConceptoIncluidoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = ConceptoIncluido
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoResponsableSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = TipoResponsable
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoSujetoSerializer(serializers.ModelSerializer):
    """ Serializador """
    class Meta:
        """ Clase """
        model = TipoSujeto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class TipoDocumentoSerializer(serializers.ModelSerializer):
    """ Serializador """
 
    idmascara = serializers.PrimaryKeyRelatedField(
        queryset=Mascara.objects.all(),
        write_only=True
    )
    idmascara_detail = MascaraSerializer(source='idmascara', read_only=True)

    class Meta:
        """ Clase """
        model = TipoDocumento
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idmascara': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class CuitPaisSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtiposujeto = serializers.PrimaryKeyRelatedField(
        queryset=TipoSujeto.objects.all(),
        write_only=True
    )

    idtiposujeto_detail = TipoSujetoSerializer(source='idtiposujeto', read_only=True)

    idpais = serializers.PrimaryKeyRelatedField(
        queryset=Pais.objects.all(),
        write_only=True
    )
    idpais_detail = MascaraSerializer(source='idpais', read_only=True)

    idtipodocumento = serializers.PrimaryKeyRelatedField(
        queryset=TipoDocumento.objects.all(),
        write_only=True
    )
    idtipodocumento_detail = TipoDocumentoSerializer(source='idtipodocumento', read_only=True)


    class Meta:
        """ Clase """
        model = CuitPais
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idtiposujeto': {'write_only': True},  # Asegura que se use en el POST
            'idmascara': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class TipoFrecuenciaSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoFrecuencia
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


class TipoValorSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = TipoValor
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')


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

class IndiceSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    idtipoindice = serializers.PrimaryKeyRelatedField(
        queryset=TipoIndice.objects.all(),
        write_only=True
    )
    idtipoindice_detail = TipoIndiceSerializer(source='idtipoindice', read_only=True)

    class Meta:
        """ Clase """
        model = Indice
        fields = '__all__'  # O especifica los campos que deseas incluir
        extra_kwargs = {
            'idtipoindice': {'write_only': True},  # Asegura que se use en el POST
        }
        read_only_fields = ('created_at', 'updated_at')

class AlicuotaImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = AlicuotaImpuesto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class PadronImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = PadronImpuesto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

class ClasificacionImpuestoSerializer(serializers.ModelSerializer):
    """ Serializador """
    
    class Meta:
        """ Clase """
        model = ClasificacionImpuesto
        fields = '__all__'  # O especifica los campos que deseas incluir
        read_only_fields = ('created_at', 'updated_at')

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

## IMPUESTOS QUE TIENEN FK A MODULOS ANTERIORES ##################################

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
