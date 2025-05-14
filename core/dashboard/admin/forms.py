from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms
from accounts.models import Profile
class AdminPasswordChangeForm(PasswordChangeForm):
        error_messages = {
       
        "password_incorrect": _(
            "رمزعبور فعلی شما اشتباه است !"
        ),
        "password_mismatch": _(" رمز عبور های جدید شما باهم تطابق ندارند!"),

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['old_password'].error_messages['required'] = _("وارد کردن رمز عبور فعلی الزامی است!")
            self.fields['new_password1'].error_messages['required'] = _("لطفاً رمز عبور جدید را وارد کنید!")
            self.fields['new_password2'].error_messages['required'] = _("تکرار رمز عبور جدید الزامی است!")

class AdminProfileForm(forms.ModelForm):
      class Meta:
            model=Profile
            fields=['first_name','last_name','phone_number']