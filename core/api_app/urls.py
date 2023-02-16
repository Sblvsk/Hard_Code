from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.ProductCategoryListAPIView.as_view(), name='category_list_create'),
    path('attributes/', views.ProductAttributeListAPIView.as_view(), name='attribute_list_create'),
    path('products/', views.ProductListAPIView.as_view(), name='product_list_create'),
]
