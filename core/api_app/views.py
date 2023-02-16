from rest_framework import generics
from mainapp.models import ProductCategory, ProductAttribute, Product
from .serializers import ProductCategorySerializer, ProductAttributeSerializer, ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryListAPIView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductAttributeListAPIView(generics.ListAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


