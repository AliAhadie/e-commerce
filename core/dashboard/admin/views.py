from django.views.generic import TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import IsAdmin
from django.contrib.auth.views import PasswordChangeView as auth_view
from .forms import AdminPasswordChangeForm,AdminProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from accounts.models import Profile
from django.shortcuts import get_object_or_404

class AdminDashboardHomeView(LoginRequiredMixin,IsAdmin,TemplateView):
    template_name='dashboard/admin/home.html'

class AdminSecurityView(LoginRequiredMixin,IsAdmin,TemplateView,SuccessMessageMixin,auth_view,):  
    form_class=AdminPasswordChangeForm
    template_name='dashboard/admin/account-security.html'
    success_message='رمز عبور با موفقیت بروزرسانی شد!'
    success_url=reverse_lazy('dashboard:admin:security-edit')

class AdminProfileView(LoginRequiredMixin, IsAdmin, SuccessMessageMixin, UpdateView):
    template_name = 'dashboard/admin/account-profile.html'
    model = Profile
    form_class = AdminProfileForm
    success_message = "Profile updated successfully."

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)