import random
from faker import Faker
Faker = Faker()

def criar_crientes(qtd):
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
    
if __name__ == "__main__":
  import os

  from django.core.wsgi import get_wsgi_application

  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
  application = get_wsgi_application()
  
  #criar_fornecedor(5)
  #criar_categoria(5)
  #criar_fabricante(5)
  #criar_produto(50)
  criar_crientes(50)

    


