from rest_framework import generics
from mainapp.models import ProductCategory, ProductAttribute, Product
from .serializers import ProductCategorySerializer, ProductAttributeSerializer, ProductSerializer


class ProductCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductAttributeListCreateView(generics.ListCreateAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


class ProductAttributeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
