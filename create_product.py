from decimal import Decimal
import random
from faker import Faker
Faker = Faker()

def criar_clientes(qtd):
  from apps.clientes.models import Cliente
  for i in range(qtd):
    c = Cliente.objects.create(
      nome = Faker.name(),
      documento = str(Faker.random_number(digits=12, fix_len=True)),
      email = Faker.email(),
      telefone = str(Faker.random_number(digits=11, fix_len=True)),
    )
    c.save()

def criar_categoria(qtd):
  from apps.produtos.models import Categoria
  for i in range(qtd):
    c = Categoria.objects.create(
      nome = Faker.name(),
    )
    c.save()
    
def criar_fabricante(qtd):
  from apps.produtos.models import Fabricante
  for i in range(qtd):
    f = Fabricante.objects.create(
      nome = Faker.name(),
    )
    f.save()
    
def criar_fornecedor(qtd):
  from apps.produtos.models import Fornecedor
  for i in range(qtd):
    f = Fornecedor.objects.create(
      nome = Faker.name(),
      documento = str(Faker.random_number()),
      telefone = str(Faker.random_number()),
      email = Faker.email(),
    )
    f.save()

def criar_produto(qtd):
  from apps.produtos.models import Produto
  from apps.produtos.models import Fornecedor
  from apps.produtos.models import Categoria
  from apps.produtos.models import Fabricante
  
  categoria = Categoria.objects.all()
  fornecedor = Fornecedor.objects.all()
  fabricante = Fabricante.objects.all()
  for i in range(qtd):
    p = Produto.objects.create(
      nome = Faker.name(),
      fabricante = random.choice(fabricante),
      categoria = random.choice(categoria),
      fornecedor = random.choice(fornecedor),
      link_produto = Faker.url(),
      preco_compra = Faker.pydecimal(left_digits=5, right_digits=2, positive=True),
    )
    p.save()
    
def criar_servico(qtd):
  from apps.produtos.models import Servico, Categoria
  categoria = Categoria.objects.all()
  for i in range(qtd):
    s = Servico.objects.create(
      nome = Faker.name(),
      categoria = random.choice(categoria),
    )
    s.save()
    
def criar_orcamento(qt):
  from apps.orcamentos.models import Orcamento, ItemProduto, ItemServico
  from apps.clientes.models import Cliente
  from apps.produtos.models import Produto, Servico
  

  for i in range(qt):
    o = Orcamento.objects.create(
      titulo = Faker.name(),
      cliente = random.choice(Cliente.objects.all()),
      descricao = Faker.name(),
    )
    o.save()
    for p in range(15):
      _produto = random.choice(Produto.objects.all()),
      produtos = ItemProduto.objects.create(
        orcamento = o,
        produto = _produto[0],
        preco = Decimal(_produto[0].preco_compra), 
        quantidade = random.randint(1, 10),
        acrescimo = Faker.pydecimal(left_digits=5, right_digits=2, positive=True),
       
      )
      print(produtos)
      produtos.save()
    for servicos in range(5):
      servicos = ItemServico.objects.create(
        orcamento = o,
        servico = random.choice(Servico.objects.all()),
        descricao = Faker.name(),
        quantidade = random.randint(1, 10),
        valor = Faker.pydecimal(left_digits=5, right_digits=2, positive=True),
       
    )
      servicos.save() 
      
     
    
if __name__ == "__main__":
  import os

  from django.core.wsgi import get_wsgi_application

  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
  application = get_wsgi_application()
  
  #criar_fornecedor(5)
  #criar_categoria(5)
  #criar_fabricante(5)
  #criar_produto(50)
  #criar_servico(10)
  #criar_clientes(10)
  criar_orcamento(1)

    


