from django.contrib import admin
from .models import Produto, Fabricante, Categoria, Fornecedor

admin.site.register(Produto)
admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Fornecedor)
