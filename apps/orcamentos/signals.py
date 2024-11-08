from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.dispatch import receiver # Import the receiver
from django.db.models import Sum, F
from decimal import Decimal, InvalidOperation
from . import models



def total_produtos(instance_orcamento):
    return sum(item_produto.total for item_produto in models.ItemProduto.objects.filter(orcamento_id=instance_orcamento.id))

def total_servicos(instance_orcamento):
    return sum(item_servico.total for item_servico in models.ItemServico.objects.filter(orcamento=instance_orcamento))

def total_compra(instance_orcamento):
    return sum(item.preco * item.quantidade for item in models.ItemProduto.objects.filter(orcamento=instance_orcamento))


@receiver(post_save, sender=models.ItemProduto)
def update_total_orcamento(sender, instance, signal, *args, **kwargs):
    
    orcamento = instance.orcamento
    total_produtos = 0
    total_mao_de_obra = 0
    total_compra = 0
    obj = models.ItemProduto.objects.filter(orcamento=orcamento)
    obj_mao_de_obra = models.ItemServico.objects.filter(orcamento=orcamento)

    for produto_item in obj:
        if not produto_item.total:
            continue
        total_produtos += produto_item.total
    for product in obj:
        total_compra += product.produto.preco_compra * product.quantidade
    for item_servico in obj_mao_de_obra:
        if not item_servico.total:
            continue
        total_mao_de_obra += item_servico.total

    _obj_produto_compra = models.ItemProduto.objects.filter(orcamento=orcamento)
    _obj_compra_mao_de_obra = models.ItemServico.objects.filter(orcamento=orcamento)
    tota_item_compra = 0
    for item_comp in _obj_produto_compra:
        tota_item_compra += item_comp.produto.preco_compra * item_comp.quantidade

    orcamento.total_equipamentos = total_produtos
    orcamento.total_mao_de_obra = total_mao_de_obra
    orcamento.total = total_produtos + total_mao_de_obra

    orcamento.total_compra = total_compra

    orcamento.total_lucro = ((total_produtos + total_mao_de_obra) - tota_item_compra)
    print(orcamento.total_lucro)
    orcamento.save()