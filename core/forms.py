from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class LogInForm(AuthenticationForm):
    model = User
    fields = ['username', 'password']

    username = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'Your user name',
         'class': 'w-full px-6 py-3 rounded-xl'
     }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))




class SigningUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your user name here',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your Email here',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full px-6 py-4 rounded-xl',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
