from django.shortcuts import render
from rest_framework import response, status as http_status
from rest_framework import  decorators as rest_decorators, permissions as rest_permissions 

from rest_framework_simplejwt import views as jwt_views, serializers as jwt_serializers

from apps.account import serializers

@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([])
def register(request):
    serializer = serializers.RegisterSerializer(data=request.data)
    
    serializer.is_valid(raise_exception=True)
    
    user = serializer.save()
    
    return response.Response(status=http_status.HTTP_201_CREATED)


class AccountTokenObtainPairSerializer(jwt_serializers.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class AccountTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = AccountTokenObtainPairSerializer
    
@rest_decorators.api_view(['GET'])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])  
def detail(request):
    serializer = serializers.AccountSerializer(request.user)
    return response.Response(serializer.data)
