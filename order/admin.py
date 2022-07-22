from django.contrib import admin

# Register your models here.
from .models import Order, ShopProductOrder

admin.site.register(Order)
admin.site.register(ShopProductOrder)