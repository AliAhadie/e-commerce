from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from accounts.models import UserType


class DashboardHomeView(LoginRequiredMixin, View):
    """base class for dashboard home"""

    def dispatch(self, request, *args, **kwargs):
        """ redirect user before request (get,post,..) """

        if request.user.is_authenticated:
            if request.user.type == UserType.admin.value:
                return redirect(reverse_lazy("dashboard:admin:home"))
            if request.user.type == UserType.customer.value:
                return redirect(reverse_lazy("dashboard:customer:home"))
        return redirect(reverse_lazy("accounts:login"))
