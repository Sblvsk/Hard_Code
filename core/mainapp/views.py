from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import ProductForm, ProductCategoryForm
from .models import Product, ProductCategory


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price', 'category']
    success_url = reverse_lazy('product_list')


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'category_form.html'
    fields = ['name', 'fields']
    success_url = reverse_lazy('category_list')