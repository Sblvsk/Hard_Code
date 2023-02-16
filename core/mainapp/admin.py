from django.contrib import admin
from .models import ProductCategory, ProductAttribute, Product

admin.site.register(ProductCategory)
admin.site.register(ProductAttribute)
admin.site.register(Product)
