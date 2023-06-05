from django.forms import ModelForm
from .models import Companies
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import User




class CompanyForm(ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']