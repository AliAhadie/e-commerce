from django.urls import path
from .views import *

app_name='shop'

urlpatterns=[
    path('grid/',ProuctsGridView.as_view(),name='products'),
    path('list/',ProductsListView.as_view(),name='list')
   
]