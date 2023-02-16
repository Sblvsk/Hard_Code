from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
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


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'mainapp/product_categories_list.html'
    context_object_name = 'categories'


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'mainapp/product_category_create.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('shop:category_list')


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('shop:category_list')
    template_name = 'mainapp/product_category_delete.html'
    context_object_name = 'category'


class ProductAttributeListView(ListView):
    model = ProductAttribute
    template_name = 'mainapp/product_attributes_list.html'
    context_object_name = 'attributes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        data_type = request.POST.get('data_type')
        if name and category_id and data_type:
            category = ProductCategory.objects.get(id=category_id)
            attribute = ProductAttribute.objects.create(
                name=name,
                category=category,
                data_type=data_type
            )
            return redirect('shop:attribute_list')
        return redirect('shop:attribute_list')


class ProductAttributeCreateView(CreateView):
    model = ProductAttribute
    template_name = 'mainapp/product_attribute_create.html'
    fields = ['name', 'category', 'data_type']
    success_url = reverse_lazy('shop:attribute_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductAttributeDeleteView(DeleteView):
    model = ProductAttribute
    success_url = reverse_lazy('shop:attribute_list')
    template_name = 'mainapp/product_attribute_delete.html'
    context_object_name = 'attributes'




