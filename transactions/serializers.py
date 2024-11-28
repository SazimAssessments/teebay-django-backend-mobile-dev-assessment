from rest_framework import serializers
from products.models import Product
from .models import Purchase, Rent

class PurchaseSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    class Meta:
        model = Purchase
        fields = ['id', 'buyer', 'seller', 'product', 'purchase_date']
        read_only_fields = ['id', 'seller', 'purchase_date']

    def get_seller(self, obj) -> int:
        return obj.seller


class RentSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    rent_option = serializers.ChoiceField(choices=Product.RentOptions.choices)
    class Meta:
        model = Rent
        fields = ['id', 'renter', 'seller', 'product', 'rent_option', 'rent_period_start_date', 'rent_period_end_date', 'total_price', 'rent_date']
        read_only_fields = ['id', 'seller', 'total_price', 'rent_date']
    
    def get_seller(self, obj) -> int:
        return obj.seller
    
    def validate_rent_option(self, value):
        if value not in dict(Product.RentOptions.choices).keys():
            raise serializers.ValidationError(f"Invalid Rent Option: {value}")
        return value
