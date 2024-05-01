
"""
Module: shopapp.forms
This module defines forms for the shop application.
"""

from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core import validators
from .models import Product, Order

class OrderForm(forms.ModelForm):
    """
    Form for creating or updating an order.
    """
    class Meta:
        model = Order
        fields = 'delivery_address', 'promocode', 'color'

class ProductForm(forms.ModelForm):
    """
    Form for creating or updating a product.
    """
    class Meta:
        model = Product
        fields = "name", "price", "description", "color", "prev"
