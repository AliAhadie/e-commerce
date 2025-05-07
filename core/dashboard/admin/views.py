from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import IsAdmin


class AdminDashboardHomeView(LoginRequiredMixin,IsAdmin,TemplateView):
    template_name='dashboard/admin/home.html'