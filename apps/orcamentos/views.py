from rest_framework import permissions, viewsets
from .models import Orcamento, ItemServico, InformacoesOrcamento, ItemProduto
from .serializers import  OrcamentoSerializer, ItemServicoSerializer, InformacoesOrcamentoSerializer, ItemProdutoSerializer

class OrcamentoViewSet(viewsets.ModelViewSet):
  queryset = Orcamento.objects.all().order_by('-created')
  serializer_class = OrcamentoSerializer
  permission_classes = [permissions.IsAuthenticated]
  
class InformacoesOrcamentoViewSet(viewsets.ModelViewSet):
  queryset = InformacoesOrcamento.objects.all().order_by('-created')
  serializer_class = InformacoesOrcamentoSerializer
  permission_classes = [permissions.IsAuthenticated]
  
class ItemProdutoViewSet(viewsets.ModelViewSet):
  queryset = ItemProduto.objects.all().order_by('-created')
  serializer_class = ItemProdutoSerializer
  permission_classes = [permissions.IsAuthenticated]
  
class ItemServicoViewSet(viewsets.ModelViewSet):
  queryset = ItemServico.objects.all().order_by('-created')
  serializer_class = ItemServicoSerializer
  permission_classes = [permissions.IsAuthenticated]
