
"""
Module: shopapp.urls
This module defines URL patterns for the shop application.
"""

from django.urls import path
from .views import (
    groups_list,
    shop_index,
    create_order,
    ProductsListView,
    ProductCreateView,
    OrdersListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    OrderDetailView,
    OrderUpdateView,
    HelloView
)

app_name = 'shopapp'

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path("", shop_index, name='shop_index'),
    path('groups/', groups_list, name='groups_list'),
    path('create/', ProductCreateView.as_view(), name='create-product'),
    path('orders/', create_order, name='create-order'),
    path('order/', OrdersListView.as_view(), name='order-list'),
    path('products/', ProductsListView.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/archived/', ProductDeleteView.as_view(), name='delete_product'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='orders_details'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='update_orders'),
]
