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

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cart=CartSession(self.request.session)
        cart_items=cart.get_cart_items()
        context['cart_items']=cart_items
        context['total_price']=cart.get_total_price()
        
        
    
        return context

