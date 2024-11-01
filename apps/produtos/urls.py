from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'fornecedores', views.FornecedoresViewSet)
router.register(r'produtos', views.ProdutosViewSet)
router.register(r'categorias', views.CategoriasViewSet)
router.register(r'fabricantes', views.FabricantesViewSet)


app_name = 'produtos'


urlpatterns = [
     path('', include(router.urls)),
]