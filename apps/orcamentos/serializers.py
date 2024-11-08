from rest_framework import serializers
import decimal
from .models import Orcamento, ItemServico, InformacoesOrcamento, ItemProduto


class OrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orcamento
        fields = '__all__'

class ItemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemServico
        fields = '__all__'

class InformacoesOrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacoesOrcamento
        fields = '__all__'
        

class ItemProdutoSerializer(serializers.ModelSerializer):
    valor_compra = serializers.SerializerMethodField()
    
    def get_valor_compra(self, instance):
        return instance.valor_compra
    class Meta:
        model = ItemProduto
        fields = ['id', 'orcamento',  'quantidade', 'acrescimo', 'preco', 'total', 'produto', 'valor_compra', 'created', 'modified']
        
    def create(self, validated_data):
            return self._create_or_update(validated_data)

    def update(self, instance, validated_data):
        return self._create_or_update(validated_data, instance)

    def _create_or_update(self, validated_data, instance=None):
        if ItemProduto.objects.filter(orcamento_id=validated_data['orcamento'].id).exists():
            instance = ItemProduto.objects.get(orcamento_id=validated_data['orcamento'].id)
            instance.quantidade += validated_data['quantidade']
            instance.preco = instance.preco * (validated_data['acrescimo'] / 100)
            instance.total = instance.preco * validated_data['quantidade']
            instance.save()
            return instance
            
        validated_data['preco'] = validated_data['produto'].preco_compra * (validated_data['acrescimo'] / 100)
        validated_data['total'] = validated_data['preco'] * validated_data['quantidade']
        instance.save()
        return instance
    
    