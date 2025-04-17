from django import template
from shop.models import Product,ProductStatus,ProductCategory

register = template.Library()

@register.inclusion_tag('includes/leatest_products.html')
def show_leatest_products():
    leatest_products=Product.objects.filter(status=ProductStatus.publish.value).order_by('-created_at')[:8]
    
    return {'leatest_products':leatest_products}

@register.inclusion_tag('includes/similar_products.html')
def show_similar_products(product):
    product_categories= product.category.all()
    similar_products=Product.objects.filter(status=ProductStatus.publish.value,category__in=product_categories)[:4]
    
    return {'similar_products':similar_products}