
"""
This Python code defines serializers for the `Group` and `Product` models using the Django REST Framework's `ModelSerializer` class. Below is the documentation for this code:

1. `from django.contrib.auth.models import Group`:
   - This import statement imports the `Group` model from Django's built-in authentication framework.

2. `from rest_framework import serializers`:
   - This import statement brings in the `serializers` module from the Django REST Framework (DRF), which provides tools for serializing and deserializing Django model instances into JSON representations.

3. `from shopapp.models import Product`:
   - This import statement imports the `Product` model from the `shopapp` application.

4. `class GroupSerializer(serializers.ModelSerializer):`:
   - This class defines a serializer for the `Group` model.
   - It inherits from the `ModelSerializer` class provided by DRF, which automatically generates serializer fields based on the model fields.

5. `class Meta:`:
   - The `Meta` inner class within the `GroupSerializer` class provides metadata configuration for the serializer.

6. `model = Group`:
   - This attribute specifies the model class that the serializer is associated with, which is the `Group` model in this case.

7. `fields = 'pk', 'name'`:
   - This attribute specifies the fields of the `Group` model that should be included in the serialized representation.

8. `class ProductSerializer(serializers.ModelSerializer):`:
   - This class defines a serializer for the `Product` model in a similar manner as the `GroupSerializer`.

9. `class Meta:`:
   - The `Meta` inner class within the `ProductSerializer` class provides metadata configuration for the serializer.

10. `model = Product`:
    - This attribute specifies the model class that the serializer is associated with, which is the `Product` model.

11. `fields = 'pk', 'name', 'description', 'color', 'price', 'preview'`:
    - This attribute specifies the fields of the `Product` model that should be included in the serialized representation.

Overall, these serializers define how instances of the `Group` and `Product` models should be serialized into JSON format, allowing them to be easily consumed by RESTful APIs.

"""

from django.contrib.auth.models import Group
from rest_framework import serializers
from  shopapp.models import Product

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = 'pk', 'name'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'pk', 'name', 'description', 'color', 'price', 'preview'