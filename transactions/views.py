from rest_framework import generics, viewsets
from .models import Purchase, Rent
from .serializers import PurchaseSerializer, RentSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    authentication_classes = []

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    authentication_classes = []
