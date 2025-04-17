from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .forms import NewsLetterForm
from .models import Newsletter


# Create your views here.

class IndexView(TemplateView):
    template_name='website/index.html'


class SubscribeView(CreateView):
    template_name='website/index.html'
    model=Newsletter
    form_class=NewsLetterForm
    success_url='/'


    
    
        
    
