
"""
Module: shopapp.views
This module contains views for managing products and orders in a shop application.
"""

import logging
from timeit import default_timer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group, User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, request, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, UpdateView, DeleteView, DetailView, CreateView
from django.utils.translation import gettext_lazy as _, ngettext
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import Product, Order
from .forms import OrderForm, ProductForm
from myapiapp.serializer import ProductSerializer

logger = logging.getLogger(__name__)

class ProductViewSet(ModelViewSet):
    """
    A viewset for handling CRUD operations on products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["name", "description"]
    filterset_fields = [
        "name",
        "description",
        "price",
        "discount",
        "archived"
    ]
    ordering_fields = [
        "name",
        "price",
        "discount",
    ]

    @extend_schema(
        summary='Get one product by ID',
        description='Retrieves a product by its ID, returns 404 if not found.',
        responses={
            200: ProductSerializer,
            404: OpenApiResponse(description='Empty response, product by ID not found'),
        }
    )
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

def shop_index(request: HttpRequest) -> HttpResponse:
    """
    View function for rendering the shop index page.
    """
    context ={
        'runtime': default_timer()
    }
    return render(request, 'shopapp/index.html', context=context)

def groups_list(request: HttpRequest) -> HttpResponse:
    """
    View function for listing all user groups.
    """
    context = {
        'groups': Group.objects.all()
    }
    return render(request, 'shopapp/groups-list.html', context=context)

class OrdersListView(LoginRequiredMixin, ListView):
    """
    View for listing orders.
    """
    model = Order
    template_name = 'shopapp/order-list.html'
    context_object_name = 'order'

class ProductDetailView(View):
    """
    View for displaying product details.
    """
    def get(self,request:HttpRequest,pk: int) -> HttpResponse:
        product = get_object_or_404(Product,pk=pk)
        context = {
            'product': product,
        }
        return render(request, 'shopapp/products-details.html', context=context)

class OrderDetailView(PermissionRequiredMixin, DetailView):
    """
    View for displaying order details.
    """
    permission_required = ["shopapp.view_order"]
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating product details.
    """
    model = Product
    fields = 'name','description','price','discount',"preview"
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse(
            'shopapp:product_details',
            kwargs={'pk': self.object.pk},
        )

class OrderUpdateView(UpdateView):
    """
    View for updating order details.
    """
    model = Order
    form_class = OrderForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'shopapp:orders_details',
            kwargs={'pk': self.object.pk},
        )

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a product.
    """
    model = Product
    success_url = reverse_lazy('shopapp:product-list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)

class ProductsListView(ListView):
    """
    View for listing products.
    """
    template_name = 'shopapp/product-list.html'
    model = Product
    context_object_name = 'products'

class ProductCreateView(UserPassesTestMixin, CreateView):
    """
    View for creating a new product.
    """
    def test_func(self):
        return self.request.user.is_superuser

    model = Product
    fields = "name", "price", "description", "discount", "preview"
    success_url = reverse_lazy("shop:products")

def create_order(request: HttpRequest) -> HttpResponse:
    """
    View function for creating a new order.
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            user_instance = User.objects.get(id=1)
            delivery_address = form.cleaned_data['delivery_address']
            promocode = form.cleaned_data['promocode']
            color = form.cleaned_data['color']
            order_instance = Order.objects.create(delivery_address=delivery_address, promocode=promocode, color=color , user =user_instance )
    else:
        form = OrderForm()

    context = {
        'form': form
    }

    return render(request, 'shopapp/create-order.html', context=context)

class HelloView(View):
    """
    A simple view for saying hello.
    """
    welcome_message = _("welcome hello world")

    def get(self, request: HttpRequest) -> HttpResponse:
        items_str = request.GET.get('items') or 0
        items = int(items_str)
        products_line = ngettext(
            "one product",
            "{count} Uploads",
            items,
        )
        products_line = products_line.format(count=items)
        return HttpResponse(
            f"<h1>{self.welcome_message}</h1>"
            f"\n<h2>{products_line}</h2>"
        )

class ProductsDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.order_by("pk").all()
        products_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": product.price,
                "is_archived": product.is_archived,
            }
            for product in products
        ]
        elem = products_data[0]
        name = elem['name']
        print(name)
        return JsonResponse({"products": products_data})