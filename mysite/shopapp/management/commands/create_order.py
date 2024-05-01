"""
This Python code defines a Django management command for creating orders in the shop application.

Description:
    - It imports necessary modules and classes from Django, including BaseCommand, User, and models.
    - It defines a custom management command named "Command" that inherits from BaseCommand.
    - The docstring of the Command class provides a brief description of its purpose, which is to create orders.
    - Within the handle method, it retrieves a specific user object from the User model.
    - It retrieves a sequence of products using Product.objects.defer() to defer loading of the 'delivery_address' field.
    - It attempts to create an Order object using the get_or_create method, specifying the delivery address, promocode, and user.
    - Finally, it outputs a message indicating whether the order was created or already existed.

Note: This command assumes the existence of a specific user with the username 'project'.

"""

from typing import Sequence

from django.contrib.auth.models import User

from django.core.management import BaseCommand

from .models import Order

from .models import Product

class Command(BaseCommand):
    """
    Creating Orders
    """
    def handle(self, *args, **options):
        self.stdout.write("")
        user = User.objects.get(username='project')
        products: Sequence[Product] = Product.objects.defer('delivery_address')

        order,created = Order.objects.get_or_create(
           delivery_address='Hanrapetuyan 22',
           promocode='hello',
            user=user,
    )

        self.stdout.write(f'Created Order: {order}')