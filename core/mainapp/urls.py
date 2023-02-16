from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('categories/', views.ProductCategoryListView.as_view(), name='category_list'),
    path('categories/create', views.ProductCategoryCreateView.as_view(), name='create_category'),
    path('categories/delete/<int:pk>', views.ProductCategoryDeleteView.as_view(), name='delete_category'),
    path('attributes/', views.ProductAttributeListView.as_view(), name='attribute_list'),
    path('attributes/create', views.ProductAttributeCreateView.as_view(), name='create_attribute'),
    path('attributes/delete/<int:pk>', views.ProductAttributeDeleteView.as_view(), name='delete_attribute'),

]
