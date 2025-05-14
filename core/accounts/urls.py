from django.urls import path, include
from .views import *

app_name = "accounts"

urlpatterns = [
    # path('',include('django.contrib.auth.urls')),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", SignUpView.as_view(), name="register"),

]
