from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core import validators
from .models import Product, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'delivery_address','promocode','color'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price","description","color","preview"