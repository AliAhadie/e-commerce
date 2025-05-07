from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..permissions import IsCustomer

class CustomerDashboardHomeView(LoginRequiredMixin,IsCustomer,TemplateView):
    template_name='dashboard/customer/home.html'