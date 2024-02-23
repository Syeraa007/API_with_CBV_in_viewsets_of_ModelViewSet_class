from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
# from rest_framework.viewsets import ModelViewSet 
from rest_framework import viewsets


# class ProductCrudActions(ModelViewSet):
class ProductCrudActions(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
