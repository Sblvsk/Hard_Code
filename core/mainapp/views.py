from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
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
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price', 'category']
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price', 'category']
    success_url = reverse_lazy('product_list')
