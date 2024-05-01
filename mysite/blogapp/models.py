
"""
This Python code defines Django models for managing articles in a blogging application. Below is the documentation for these models:

1. `from django.db import models`:
   - This import statement imports the `models` module from Django, which provides classes for defining database models.

2. `class Author(models.Model):`:
   - This class represents an author of an article.
   - It inherits from Django's `Model` class, indicating that it's a database model.
   - Attributes:
     - `name`: A `CharField` storing the name of the author with a maximum length of 100 characters.
     - `bio`: A `TextField` for storing the biography or description of the author.

3. `class Category(models.Model):`:
   - This class represents a category to which an article belongs.
   - Attributes:
     - `name`: A `CharField` storing the name of the category with a maximum length of 40 characters.

4. `class Tag(models.Model):`:
   - This class represents a tag associated with an article.
   - Attributes:
     - `name`: A `CharField` storing the name of the tag with a maximum length of 20 characters.

5. `class Article(models.Model):`:
   - This class represents an article.
   - Attributes:
     - `title`: A `CharField` storing the title of the article with a maximum length of 200 characters.
     - `content`: A `TextField` for storing the content or body of the article.
     - `pub_date`: A `DateTimeField` representing the publication date and time of the article.
     - `author`: A `ForeignKey` relationship with the `Author` model, indicating the author of the article. It uses the `on_delete=models.CASCADE` parameter to specify that when an author is deleted, all associated articles should also be deleted.
     - `category`: A `ForeignKey` relationship with the `Category` model, indicating the category to which the article belongs. It also uses `on_delete=models.CASCADE` for cascading deletion.
     - `tags`: A `ManyToManyField` relationship with the `Tag` model, representing the tags associated with the article.

These models define the structure of the database tables for managing authors, categories, tags, and articles in the blogging application.

"""

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=40)

class Tag(models.Model):
    name = models.CharField(max_length=20)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
