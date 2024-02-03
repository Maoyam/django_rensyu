from django.shortcuts import render
from django.views.generic.edit import UpdateView
from ..models import Product

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'
