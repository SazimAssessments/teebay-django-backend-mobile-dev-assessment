from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', views.UserListView.as_view(), name='users'),
]
