
"""
This Python code defines a class-based view for rendering a list of articles in the `blogapp`. Below is the documentation for this code:

1. `from django.shortcuts import render`:
   - This import statement imports the `render` function from Django's shortcuts module, which is used to render HTML templates with context data.

2. `from django.views.generic import ListView`:
   - This import statement imports the `ListView` class from Django's generic views module, which is a class-based view for displaying a list of objects.

3. `from .models import Article`:
   - This import statement imports the `Article` model from the current package (or app), which contains information about blog articles.

4. `class ArticleListView(ListView):`:
   - This class represents a list view for displaying articles.
   - It inherits from the `ListView` class, indicating that it is a class-based view for displaying a list of objects.

5. `template_name = 'blogapp/article_list.html'`:
   - This attribute specifies the template file to be used for rendering the list of articles. In this case, it is set to `'blogapp/article_list.html'`.

6. `context_object_name = 'articles'`:
   - This attribute specifies the name of the context variable that will contain the list of articles when rendering the template. In this case, it is set to `'articles'`.

7. `queryset = (`:
   - This attribute specifies the queryset of articles to be displayed in the list view.
   - It uses a queryset that selects related objects (author, category, and tags) to optimize database queries and prefetch related objects for performance.

Overall, this class-based view provides a convenient way to render a list of articles from the database using a specified template file and context variable.

"""

from django.shortcuts import render
from django.views.generic import ListView

from  .models import Article

class ArticleListView(ListView):
    template_name = 'blogapp/article_list.html'
    context_object_name = 'articles'
    queryset = (
        Article.objects
        .select_related('author')
        .select_related('category')
        .prefetch_related('tags')
    )