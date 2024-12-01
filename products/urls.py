
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "products"
router = DefaultRouter()
router.register(r'', views.ProductViewSet, basename='product')

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path("", include(router.urls)),
]
