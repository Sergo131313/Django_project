from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Product, Order

class OrderInline(admin.TabularInline):
    """
    Inline for displaying orders in the product admin.
    """
    model = Product.orders.through

@admin.action(description='Archive Products')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    """
    Action to mark selected products as archived.
    """
    queryset.update(is_archived=True)

@admin.action(description='Unarchive Products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    """
    Action to mark selected products as unarchived.
    """
    queryset.update(is_archived=False)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for managing products.
    """
    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv'
    ]
    inlines = [
        OrderInline,
    ]
    list_display = 'pk', 'name', 'description_short','price','created_at','is_archived','color','preview'
    list_display_links = 'pk', 'name'
    ordering = '-name', 'pk'
    search_fields = 'name','color','preview'
    fieldsets = [
        (None, {
            'fields': ('name', 'description'),
        }),
        ('Color options',{
            'fields':('color',),
            'classes': ('collapse',)
        }),
        ('Picture options',{
            'fields':('preview',),
            'classes': ('collapse',)
        }),
        ('Price options', {
            'fields': ('price', 'discount'),
            'classes': ('collapse', 'wide')
        }),
        ('Extra options', {
            'fields': ('is_archived',),
            'classes': ('collapse',),
            'description': 'Extra options. Field "archived" is for soft delete',
        })
    ]

    def description_short(self, obj: Product) -> str:
        """
        Returns a short description of the product.
        """
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'


class ProductInline(admin.StackedInline):
    """
    Inline for displaying products in the order admin.
    """
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin class for managing orders.
    """
    inlines = [
        OrderInline,
    ]
    list_display = 'pk', 'delivery_address', 'promocode', 'user_verbose', 'created_at'

    def get_queryset(self, request):
        """
        Returns the queryset for orders with user prefetching.
        """
        return Order.objects.select_related('user').prefetch_related('Uploads')

    def user_verbose(self, obj: Order) -> str:
        """
        Returns a verbose representation of the user.
        """
        return obj.user.first_name or obj.user.username