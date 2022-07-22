from rest_framework  import serializers

from .models import Product, Category, ShopProduct

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name_category', 
                    )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name_product', 
                    'description', 
                    'characteristics',
                    'category',
                    )


    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instanse, validated_data):
        instanse.name_product = validated_data.get('name_product', instanse.name_product)
        instanse.description = validated_data.get('description', instanse.description)
        instanse.characteristics = validated_data.get('characteristics', instanse.characteristics)
        instanse.category = validated_data.get('category', instanse.category)
        instanse.save()
        return instanse



class ShopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProduct
        # fields = ('price', 'quantity', )
        fields = '__all__'