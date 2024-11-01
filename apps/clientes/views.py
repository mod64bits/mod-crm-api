from rest_framework import permissions, viewsets
from .models import Cliente
from .serializers import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all().order_by('-created')
  serializer_class = ClienteSerializer
  permission_classes = [permissions.IsAuthenticated]
