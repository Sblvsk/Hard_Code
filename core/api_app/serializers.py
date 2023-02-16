from rest_framework import serializers
from mainapp.models import ProductCategory, ProductAttribute, Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    attributes = ProductAttributeSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


