from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EducationHistory, Profile, Skill, Qualification, EducationHistory, EmploymentHistory 


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField()
    phoneNumber = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email','address','phoneNumber', 'password1', 'password2']


class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = (
            'qualification',
        )

class EducationHistoryForm(forms.ModelForm):
    class Meta:
        model = EducationHistory
        fields = (
            'degree',
            'date',
            'university',
            'country',
        )

class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = (
            'title',
            'period',
            'company',
            'city',
            'location'
        )

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = (
            'name',
        )
        


