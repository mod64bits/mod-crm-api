from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.ClientesViewSet)

app_name = 'clientes'

urlpatterns = [
     path('', include(router.urls)),
]