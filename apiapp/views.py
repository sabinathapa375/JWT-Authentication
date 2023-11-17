from django.shortcuts import render
from .serializers import ProductSerializetrs
from .models import Product
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializetrs
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    