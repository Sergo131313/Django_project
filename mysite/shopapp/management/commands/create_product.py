
"""
This Python script defines a management command for creating products in the shop application.

Description:
    - It imports BaseCommand from django.core.management and Product model from the shop application.
    - It defines a Command class that inherits from BaseCommand. This class represents the management command for creating products.
    - The handle method is overridden to implement the logic for creating products.
    - Inside the handle method:
        - It outputs a message indicating the start of the product creation process.
        - It defines lists containing product names and their corresponding prices.
        - It iterates over the lists of products and prices simultaneously using the zip function.
        - For each product and price pair, it attempts to retrieve an existing product with the same name from the Product model. If the product doesn't exist, it creates a new one.
        - It outputs a message indicating the successful creation of each product.
        - Finally, it outputs a success message indicating that all products have been created.

Note: This management command can be executed via the Django management CLI to create products in the system.

"""

from django.core.management import BaseCommand

from .models import Product


class Command(BaseCommand):
    """
    Create product:
    """

    def handle(self, *args, **options):
        self.stdout.write('Create Product')

        products = [
            'Laptop',
            'Smartphone',
            'Desktop'
        ]

        prices = [
            1999,
            2999,
            999
        ]

        for products,price in zip(products,prices):

            name,created = Product.objects.all().get_or_create(name=products, price=price)
            self.stdout.write(f'Create product: {name} for  ${price}')
        self.stdout.write(self.style.SUCCESS('Products Created'))