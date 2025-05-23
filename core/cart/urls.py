from django.urls import path
from .views import (SessionAddProductView,SessionCartSummery,SessionUpdateProductView,SessionDeleteProductView)

app_name='cart'

urlpatterns = [
    path('session/add-product/',SessionAddProductView.as_view(),name='session_add_product'),
    path('session/cart-summery/',SessionCartSummery.as_view(),name='session_cart_summary'),
    path('session/update-product/',SessionUpdateProductView.as_view(),name='session_update_product'),
    path('session/delete-product/',SessionDeleteProductView.as_view(),name='session_delete_product'),
]