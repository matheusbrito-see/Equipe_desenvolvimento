from rest_framework import serializers
from .models import Setor, Usuario, TipoMaterial, AreaUtilizacao, UnidadeMedia, Item, Listaplanejamento, ItensLista
from lista_cadastro.models import itemPlanejado

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TipoMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMaterial
        fields = '__all__'
        
class AreaUtilizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaUtilizacao
        fields = '__all__'
        
class UnidadeMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeMedia
        fields = '__all__'
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class ListaplanejamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listaplanejamento
        fields = '__all__'
        
class ItensListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensLista
        fields = '__all__'
        
class ItemPlanejadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = itemPlanejado
        fields = '__all__'
        
class ItensListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensLista
        fields = '__all__'