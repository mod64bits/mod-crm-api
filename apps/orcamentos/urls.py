from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrcamentoViewSet)
router.register(r'informacoes', views.InformacoesOrcamentoViewSet)
router.register(r'item-produto', views.ItemProdutoViewSet)
router.register(r'item-servicos', views.ItemServicoViewSet)

app_name = 'orcamentos'

urlpatterns = [
     path('', include(router.urls)),
]