from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views


app_name = 'account'


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.AccountTokenObtainPairView.as_view(), name='login'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='refresh'),
    path('logout', jwt_views.TokenBlacklistView.as_view(), name='logout'),
    path('user', views.detail, name='user'),
]