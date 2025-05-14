from django.urls import path
from dashboard.admin.views import(AdminDashboardHomeView,AdminProfileView)
from .views import AdminSecurityView

app_name='admin'

urlpatterns=[
    path('home/',AdminDashboardHomeView.as_view(),name='home'),
    path('security-edit/',AdminSecurityView.as_view(),name='security-edit'),
    path('profile-edit/',AdminProfileView.as_view(),name='profile-edit')
]