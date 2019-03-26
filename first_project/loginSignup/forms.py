from django import forms
from .models import profile
from django.contrib.auth.models import User


class Signup_form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'password', 'email')




