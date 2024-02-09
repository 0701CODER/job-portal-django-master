from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(
        label='name and surname',
        widget=forms.TextInput(
           attrs={'placeholder': 'For example: Vasanth',}
           )
        )
    email = forms.EmailField(
        label='email address',
        widget=forms.EmailInput(
           attrs={'placeholder': 'Enter your email address'}
            )
        )
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}
            )
        )
    password2 = forms.CharField(
        label='repeat the password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Repeat your password'}
            )
        )
    
    error_messages = {
        'password_mismatch': "password not equal",
    }
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email has already been used")
        return email

    class Meta:
        model = User
        fields=['full_name', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='email address',
        widget=forms.EmailInput(
           attrs={'placeholder': 'Enter your email address'}
        )
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}
        )
    )