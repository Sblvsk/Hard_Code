from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView
from django.urls import reverse_lazy

from .forms import ProductForm, ProductCategoryForm
from .models import Product, ProductCategory


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_context_data(self, pk=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.all()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = Product.objects.filter(category=category)
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


