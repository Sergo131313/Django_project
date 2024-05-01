
"""
This Python code defines a Django application configuration for the blogging application. Below is the documentation for this configuration:

1. `from django.apps import AppConfig`:
   - This import statement imports the `AppConfig` class from the `apps` module in Django, which is used to configure Django applications.

2. `class BlogappConfig(AppConfig):`:
   - This class represents the configuration for the blogging application.
   - It inherits from Django's `AppConfig` class, indicating that it's an application configuration.
   - Attributes:
     - `default_auto_field`: This attribute specifies the default primary key field type for models in this application. In this case, it's set to `'django.db.models.BigAutoField'`, indicating that a big integer field will be used as the primary key for models by default.
     - `name`: This attribute specifies the name of the Django application. In this case, it's set to `'blogapp'`.

This configuration class provides settings and metadata for the blogging application, such as the default primary key field type and the application name.

"""

from django.apps import AppConfig


class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'
