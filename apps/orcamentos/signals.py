from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.dispatch import receiver # Import the receiver
from . import models


def total_produtos(instance_orcamento):
    return sum(item_produto.total for item_produto in models.ItemProduto.objects.filter(orcamento=instance_orcamento))

def total_servicos(instance_orcamento):
    return sum(item_servico.total for item_servico in models.ItemServico.objects.filter(orcamento=instance_orcamento))

def total_compra(instance_orcamento):
    return sum(item.preco * item.quantidade for item in models.ItemProduto.objects.filter(orcamento=instance_orcamento))


@receiver(post_save, sender=[models.ItemServico, models.ItemProduto, models.Orcamento])
def update_total_orcamento(sender, instance, created, updated, **kwargs):
     total_produtos = 0
     total_servicos = 0
     total_compra = 0
     orcamento = instance.orcamento
     
     if models.ItemProduto.objects.filter(orcamento=orcamento).exists():
         total_produtos = total_produtos(orcamento)
         orcamento.total = total_produtos
         total_compra = total_compra(orcamento)
         orcamento.total_compra = total_compra
         orcamento.save()
         
     if models.ItemServico.objects.filter(orcamento=orcamento).exists():
         total_servicos = total_servicos(orcamento)
         orcamento.total_servicos = total_servicos
         orcamento.save()