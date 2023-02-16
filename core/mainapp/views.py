from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product, ProductCategory, ProductAttribute


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_context_data(self, pk=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.all()
        context["attributes"] = ProductAttribute.objects.all()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        attributes = self.request.GET.get('attributes')
        if category and attributes:
            queryset = Product.objects.filter(category=category, attributes=attributes)
        elif category:
            queryset = Product.objects.filter(category=category)
        elif attributes:
            queryset = Product.objects.filter(attributes=attributes)
        return queryset


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'mainapp/product_update.html'
    fields = ['name', 'description', 'price', 'category']
    success_url = reverse_lazy('shop:product_list')


