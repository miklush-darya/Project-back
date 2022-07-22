import imp
from django.contrib import admin

# Register your models here.

from .models import Category, Product, ShopProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShopProduct)
