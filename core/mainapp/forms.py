from django import forms

from .models import Product, ProductCategory


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['avatar', 'name', 'description', 'price', 'category', 'attributes']
