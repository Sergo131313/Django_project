
"""
Module: shopapp.apps
This module defines the configuration for the shop application.
"""

from django.apps import AppConfig

class ShopappConfig(AppConfig):
    """
    Configuration class for the shop application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopapp'
