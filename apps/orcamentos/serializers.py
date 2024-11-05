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
    class Meta:
        model = ItemProduto
        fields = '__all__'
        
    def create(self, validated_data):
            return self._create_or_update(validated_data)

    def update(self, instance, validated_data):
        return self._create_or_update(validated_data, instance)

    def _create_or_update(self, validated_data, instance=None):
        orcamento = Orcamento.objects.get(id=self.context['view'].kwargs['pk'])
        produto_id = validated_data['produto'].id
        qt = validated_data['quantidade']
        percent = decimal.Decimal(validated_data['porcentagem'])
        
        # Caso já exista um produto no orçamento
        if instance is None:
            if ItemProduto.objects.filter(produto_id=produto_id, orcamento=orcamento).exists():
                instance = ItemProduto.objects.get(produto_id=produto_id, orcamento=orcamento)
                instance.quantidade += qt
            else:
                instance = ItemProduto(produto_id=produto_id, orcamento=orcamento, **validated_data)
                instance.quantidade = qt
        else:
            instance.quantidade = qt  # Atualiza a quantidade para o valor do update

        # Atualiza outros campos
        instance.porcentagem = percent
        instance.preco = self.valor_porcentagem(percent, validated_data['produto'].preco_compra)
        instance.total = instance.preco * instance.quantidade
        instance.save()
        return instance

    def valor_porcentagem(self, percent, preco_compra):
        return decimal.Decimal(preco_compra) * (percent / 100)


