
"""
This Python code defines URL patterns for the API views in the `myapiapp` application. Below is the documentation for this code:

1. `from django.urls import path`:
   - This import statement brings in the `path` function from Django's URL patterns module.
   - The `path` function is used to define URL patterns for routing requests to specific views.

2. `from .views import hello_world_view, GroupListView`:
   - This import statement imports the `hello_world_view` function and the `GroupListView` class from the views module of the current application (`myapiapp`).

3. `app_name = 'myapiapp'`:
   - This variable defines the namespace for the URL patterns defined in this module. It helps in namespacing URLs and avoiding conflicts with URLs from other applications.

4. `urlpatterns = [...]`:
   - This list variable contains the URL patterns for the API views.
   - Each URL pattern is defined using the `path` function.

5. `path('hello/', hello_world_view, name='hello')`:
   - This URL pattern maps requests with the path `/hello/` to the `hello_world_view` function.
   - The `name` parameter specifies the name of this URL pattern, which can be used to reference it in templates or code.

6. `path('groups/', GroupListView.as_view(), name='groups')`:
   - This URL pattern maps requests with the path `/groups/` to the `GroupListView` class-based view.
   - The `as_view()` method is called to convert the class-based view into a callable view.
   - The `name` parameter specifies the name of this URL pattern.

Overall, these URL patterns define endpoints for accessing the `hello_world_view`

"""

from django.urls import path
from .views import hello_world_view, GroupListView

app_name = 'myapiapp'

urlpatterns = [
    path('hello/', hello_world_view, name='hello'),
    path('groups/', GroupListView.as_view(), name='groups'),
]