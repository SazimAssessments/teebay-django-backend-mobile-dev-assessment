from rest_framework import generics, viewsets, status, parsers
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Product
from .serializers import ProductSerializer, CategorySerializer

class CategoryListView(generics.ListAPIView):
    authentication_classes = []
    serializer_class = CategorySerializer

    @extend_schema(
        responses={
            200: CategorySerializer(many=True)
        }
    )
    def get(self, request):
        categories = [
            {"value": category[0], "label": category[1]}
            for category in Product.Categories.choices
        ]
        return Response(categories, status=status.HTTP_200_OK)

class ProductViewSet(viewsets.ModelViewSet):
    parser_classes = [parsers.MultiPartParser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = []
