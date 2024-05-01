import logging
from timeit import default_timer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import Group, User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, UpdateView, DeleteView, DetailView,CreateView
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

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["name", "description",]
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
        description='Retrieves **product**, returns 404 if not found',
        responses={
            200: ProductSerializer,
            404: OpenApiResponse(description='Empty response, product by id not found'),
        }
    )
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)


def shop_index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse('<h1>Hello Shop Index</1>')

    context ={
        'runtime': default_timer()
    }

    return render(request, 'shopapp/index.html', context=context)

def groups_list(request: HttpRequest) -> HttpResponse:
    context = {
        'groups': Group.objects.all()
    }
    return render(request, 'shopapp/groups-list.html', context=context)

#def orders_list(request: HttpRequest) -> HttpResponse:
#   context = {
#        'orders': Order.objects.all()
#   }
#
#    return render(request, 'shopapp/order-list.html', context=context)

class OrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'shopapp/order-list.html'
    context_object_name = 'order'

class ProductDetailView(View):
    def get(self,request:HttpRequest,pk: int) -> HttpResponse:
        # product = Product.objects.get(pk=pk)
        product = get_object_or_404(Product,pk=pk)
        context = {
            'product': product,
        }
        return render(request, 'shopapp/products-details.html', context=context)

class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ["shopapp.view_order",]
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    fields = 'name','description','price','discount',"preview"
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse(
            'shopapp:product_details',
            kwargs={'pk': self.object.pk},
        )

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'shopapp:orders_details',
            kwargs={'pk': self.object.pk},
        )

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:product-list')

    def form_valid(self,form):
        success_url = self.get_success_url()
        self.object.archived =True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ProductsListView(ListView):
    template_name = 'shopapp/product-list.html'
    model = Product
    context_object_name = 'products'


#def create_products(request: HttpRequest) -> HttpResponse:
#    if request.method == 'POST':
#        form = ProductForm(request.POST)
#
#        if form.is_valid():
#            name = form.cleaned_data['name']
#            price = form.cleaned_data['price']
#            Product.objects.create(name=name, price=price)
#    else:
#        form = ProductForm()
#
#    context = {
#    'form' : form
#
#    }
#    return render(request, 'shopapp/create-product.html', context=context)

class ProductCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        # return self.request.user.groups.filter(name='secret-group').exists()
        return self.request.user.is_superuser

    model = Product
    fields = "name", "price", "description", "discount", "preview"
    # form_class = ProductForm
    success_url = reverse_lazy("shop:products")

def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            # form.instance.user = request.user.id
            # form.save()
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