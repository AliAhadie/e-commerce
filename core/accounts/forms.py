from django.contrib.auth import forms as auth_form
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
    
        

class AuthenticationForm(auth_form.AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_verified:
            raise ValidationError("user must verified!")
