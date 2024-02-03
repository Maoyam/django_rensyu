from django.shortcuts import render
from django.views.generic.edit import CreateView
from ..models import Product

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'