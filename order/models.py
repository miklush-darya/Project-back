from django.db import models

# Create your models here.

from django.db import models
from user.models import User

# Create your models here.
from core.models import BaseModel


class Order(BaseModel):


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f"Order {self.id}"


class ShopProductOrder(BaseModel):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="shop_product_orders")
    shopproduct = models.ForeignKey(
        "prod_and_cat.ShopProduct", on_delete=models.CASCADE, related_name="shop_product_orders_tw"
    )

    def __str__(self):
        return str(self.id)