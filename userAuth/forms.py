from django import forms
from django.forms.widgets import PasswordInput, EmailInput

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from . models import User

class MyUserCreationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    email = forms.EmailField(widget=EmailInput())
    password = forms.CharField(widget=PasswordInput())