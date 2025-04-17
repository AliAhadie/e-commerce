
from django.urls import path,include
from . import views

app_name='website'

urlpatterns = [
  
    path('',views.IndexView.as_view(),name='index'),
    path('subscribe/',views.SubscribeView.as_view(),name='subscribe')
]