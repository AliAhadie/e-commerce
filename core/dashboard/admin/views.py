from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import IsAdmin
from django.contrib.auth.views import PasswordChangeView as auth_view
from .forms import AdminPasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class AdminDashboardHomeView(LoginRequiredMixin,IsAdmin,TemplateView):
    template_name='dashboard/admin/home.html'

class AdminSecurityView(LoginRequiredMixin,IsAdmin,TemplateView,SuccessMessageMixin,auth_view,):  
    form_class=AdminPasswordChangeForm
    template_name='dashboard/admin/account-security.html'
    success_message='رمز عبور با موفقیت بروزرسانی شد!'
    success_url=reverse_lazy('dashboard:admin:security-edit')
