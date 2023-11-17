from .models import Product
from rest_framework import serializers

class ProductSerializetrs(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'name', 'price', 'description']
        