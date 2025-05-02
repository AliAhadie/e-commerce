from django.urls import path
from .views import SessionAddProductView

app_name='cart'

urlpatterns = [
    path('session/add-product/',SessionAddProductView.as_view(),name='session_add_product'),
]