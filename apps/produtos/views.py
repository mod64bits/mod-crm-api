from rest_framework import permissions, viewsets
from .models import Fabricante, Fornecedor, Categoria, Produto, Servico
from .serializers import FabricanteSerializer, FornecedorSerializer, CategoriaSerializer, ProdutoSerializer, ServicoSerializer

class FornecedoresViewSet(viewsets.ModelViewSet):
   queryset = Fornecedor.objects.all().order_by('-created')
   serializer_class = FornecedorSerializer
   permission_classes = [permissions.IsAuthenticated]
  
class FabricantesViewSet(viewsets.ModelViewSet):
   queryset = Fabricante.objects.all().order_by('-created')
   serializer_class = FabricanteSerializer
   permission_classes = [permissions.IsAuthenticated]

class CategoriasViewSet(viewsets.ModelViewSet):
   queryset = Categoria.objects.all().order_by('-created')
   serializer_class = CategoriaSerializer
   permission_classes = [permissions.IsAuthenticated]

class ProdutosViewSet(viewsets.ModelViewSet):
   queryset = Produto.objects.all().order_by('-created')
   serializer_class = ProdutoSerializer
   permission_classes = [permissions.IsAuthenticated]
   
   
class ServicosViewSet(viewsets.ModelViewSet):
   queryset = Servico.objects.all().order_by('-created')
   serializer_class = ServicoSerializer
   permission_classes = [permissions.IsAuthenticated]