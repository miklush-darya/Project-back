from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import generics
from .models import Category, Product, ShopProduct
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.

class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request):
        new_category= Category.objects.create(
            name_category=request.data['name_category'],
                )
 
        return Response({'new_category': model_to_dict(new_category)})


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def post(self, request):

        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
 
        return Response({'new_product': serializer.data})

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
 
        return Response({"product_update": serializer.data})