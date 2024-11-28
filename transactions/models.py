from django.db import models
from users.models import User
from products.models import Product
from decimal import Decimal
import logging


class Purchase(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    purchase_date = models.DateTimeField(auto_now_add=True)

    @property
    def seller(self):
        return self.product.seller.id

    def __str__(self):
        return f"Purchase {self.id} - {self.buyer.email}"


class Rent(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rents')
    rent_period_start_date = models.DateTimeField()
    rent_period_end_date = models.DateTimeField()
    rent_option = models.CharField(max_length=10, choices=Product.RentOptions.choices)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rent_date = models.DateTimeField(auto_now_add=True)


    @property
    def seller(self):
        return self.product.seller.id

    def save(self, *args, **kwargs):
        if not self.total_price:
            duration = (self.rent_period_end_date - self.rent_period_start_date).total_seconds()
            if self.rent_option == Product.RentOptions.PER_HOUR:
                hours = duration // 3600
                self.total_price = Decimal(hours) * self.product.rent_price
            elif self.rent_option == Product.RentOptions.PER_DAY:
                days = duration // 86400
                self.total_price = Decimal(days) * self.product.rent_price
        super().save(*args, **kwargs)
