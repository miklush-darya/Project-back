from django.db import models
# import jsonfield

# Create your models here.

from user.models import Shop
from core.models import BaseModel


class Category(BaseModel):

    name_category = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name_category


class Product(BaseModel):

    name_product = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    characteristics = models.TextField(blank=True)
    # characteristics = models.JSONField(blank=True)

    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name_product


class ShopProduct(BaseModel):

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="shop_roducts")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_roducts_tw")

    def __str__(self):
        return str(self.id)