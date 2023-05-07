from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile 


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField()
    phoneNumber = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email','address','phoneNumber', 'password1', 'password2']




