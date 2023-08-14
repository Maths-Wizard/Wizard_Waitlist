from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    # path('users/', views.UserListApiView.as_view(), name='users'),
    path('join/', views.UserRegister.as_view(), name='register'),
]
