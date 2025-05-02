from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import JsonResponse    
from .cart import CartSession

class SessionAddProductView(View):
    def post(self, request, *args, **kwargs):
        cart=CartSession(request.session)
        product_id = request.POST.get('product_id')
        cart.add_product(product_id)
        cart.save()
        return JsonResponse({'cart':cart._cart,'total_quntity':cart.get_quntity()})


class SessionCartSummery(TemplateView):
    template_name = 'cart/cart-summery.html'
    
