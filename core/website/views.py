from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import NewsLetterForm
from .models import Newsletter
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View 

# Create your views here.


class IndexView(View):
    def get(self,request):
    
        return render(request, "website/index.html")





class SubscribeView(CreateView):
    template_name = "website/index.html"
    model = Newsletter
    form_class = NewsLetterForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return HttpResponse("email not valid")
