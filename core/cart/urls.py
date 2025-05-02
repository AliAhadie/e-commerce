from django.urls import path
from .views import SessionAddProductView,SessionCartSummery

app_name='cart'

urlpatterns = [
    path('session/add-product/',SessionAddProductView.as_view(),name='session_add_product'),
    path('session/cart-summery/',SessionCartSummery.as_view(),name='session_cart_summary'),
]