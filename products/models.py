from django.db import models
from users.models import User
from multiselectfield import MultiSelectField

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Categories(models.TextChoices):
        ELECTRONICS = 'electronics', 'Electronics'
        FURNITURE = 'furniture', 'Furniture'
        HOME_APPLIANCES = 'home_appliances', 'Home Appliances'
        SPORTING_GOODS = 'sporting_goods', 'Sporting Goods'
        OUTDOOR = 'outdoor', 'Outdoor'
        TOYS = 'toys', 'Toys'

    
    categories = MultiSelectField(choices=Categories.choices, max_length=255)
    product_image = models.ImageField(upload_to='product_images/')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class RentOptions(models.TextChoices):
        PER_HOUR = 'hour', 'Per Hour',
        PER_DAY = 'day', 'Per Day'
    
    rent_option = models.CharField(max_length=10, choices=RentOptions.choices)
    
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
