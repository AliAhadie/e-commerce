from django.shortcuts import render
from django.contrib.auth import views as auth_view
from .forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponseRedirect

from .forms import RegisterForm
from django.views.generic.edit import CreateView

from django.views.generic import TemplateView
from django.contrib.auth import login

# Create your views here.

    
class LoginView(auth_view.LoginView):
    template_name = "accounts/page-login-simple.html"
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm


class LogoutView(auth_view.LogoutView):
    pass


from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views import View
from django.shortcuts import render, redirect


class SignUpView(View):
    template_name = "accounts/page-signup-simple.html"

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # لاگین بعد از ثبت‌نام
            return redirect('/')  # یا هر صفحه‌ای که می‌خوای
        return render(request, self.template_name, {'form': form})