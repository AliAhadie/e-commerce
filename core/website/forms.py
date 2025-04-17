from django import forms
from .models import Newsletter


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model=Newsletter
        fields = ['email']

        
