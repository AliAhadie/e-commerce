from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ProuctsGridView(TemplateView):
    template_name='shop/products-grid.html'

class ProductsListView(TemplateView):
    template_name='shop/products-list.html'