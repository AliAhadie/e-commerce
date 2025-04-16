from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductStatus,ProductCategory
from django.core.exceptions import FieldError

# Create your views here.


class ProuctsGridView(ListView):
    
    template_name = "shop/products-grid.html"
    paginate_by=5

    def get_queryset(self):
        queryset = Product.objects.filter(status=ProductStatus.publish.value)
        if search_product := self.request.GET.get("q"):
            queryset = queryset.filter(title__icontains=search_product)
            return queryset
        if search_category := self.request.GET.get('category_id'):
            queryset = queryset.filter(category__id=search_category)
        if min_price:=self.request.GET.get('min_price'):
            queryset = queryset.filter(price__gte=min_price)    
        if max_price:=self.request.GET.get('max_price') :
            queryset = queryset.filter(price__lte=max_price)   
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size',self.paginate_by)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_products"] = Product.objects.filter(
            status=ProductStatus.publish.value
        ).count()
        context['category']=ProductCategory.objects.all()
        return context



class ProductsListView(ListView):
    template_name = "shop/products-list.html"
    paginate_by = 9
    queryset = Product.objects.filter(status=ProductStatus.publish.value)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_products"] = self.queryset.count()
        return context


class ProductDetailView(DetailView):
    template_name = "shop/product-overview.html"
    queryset = Product.objects.filter(status=ProductStatus.publish.value)
