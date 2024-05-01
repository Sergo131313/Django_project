
"""
This Django model defines a Profile class that extends the models.Model class. It represents additional information associated with a user in the application.

Description:
    - It imports the User model from django.contrib.auth.models and the models module from Django.
    - It defines a Profile model with fields and behaviors.
    - The Profile model has a one-to-one relationship with the User model using a OneToOneField. This relationship links each profile to a single user.
    - The on_delete=models.CASCADE argument specifies the behavior when the associated user is deleted. CASCADE ensures that when the associated user is deleted, the profile is also deleted.

Note: This Profile model is used to store additional information about each user in the application, such as user-specific settings or preferences.

"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)