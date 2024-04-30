from django.urls import path
from .views import ArticleListView

app_name = 'blogapp'

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles')
]