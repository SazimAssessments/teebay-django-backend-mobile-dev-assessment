from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'transactions'
router = DefaultRouter()
router.register(r'purchases', views.PurchaseViewSet, basename='purchase')
router.register(r'rentals', views.RentViewSet, basename='rental')

urlpatterns = [
    path('', include(router.urls)),
]

