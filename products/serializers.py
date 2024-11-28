from rest_framework import serializers, fields
from .models import Product

class CategorySerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    categories = fields.MultipleChoiceField(choices=Product.Categories.choices)
    product_image = serializers.ImageField(required=True)
    rent_option = serializers.ChoiceField(choices=Product.RentOptions.choices)
    
    class Meta:
        model = Product
        fields = ['id', 'seller', 'title', 'description', 'categories', 'product_image', 'purchase_price', 'rent_price', 'rent_option', 'date_posted']
        read_only_fields = ['id', 'date_posted']

    def validate_categories(self, value):
        invalid_categories = [category for category in value if category not in dict(Product.Categories.choices).keys()]
        if invalid_categories:
            raise serializers.ValidationError(f"Invalid categories: {', '.join(invalid_categories)}")
        return value

