from django.shortcuts import render
from django.views.generic import ListView
from . models import Product,ProductStatus

# Create your views here.

class ProuctsGridView(ListView):
    template_name='shop/products-grid.html'
    queryset=Product.objects.filter(status=ProductStatus.publish.value)
    paginate_by=9
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['total_products']=self.queryset.count()
        return context


class ProductsListView(ListView):
    template_name='shop/products-list.html'
    paginate_by=9
    queryset=Product.objects.filter(status=ProductStatus.publish.value)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['total_products']=self.queryset.count()
        return context
