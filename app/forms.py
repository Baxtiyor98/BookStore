from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Add_category(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class Login(forms.Form):
    username = forms.CharField(label='Username' , max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']