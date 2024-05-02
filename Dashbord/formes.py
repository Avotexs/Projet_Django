from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

#register form
class CreateUserForm(UserCreationForm):
        class Meta:
              model = User
              fields = ['username', 'email', 'password1','password2']

#Authenticate
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)