from django.shortcuts import render
from django.views.generic import ListView
from ..models import Product

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 3