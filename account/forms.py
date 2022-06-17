from django import forms
from .models import UserBase


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required!')
    email = forms.EmailField(label='Enter Email', max_length=100, help_text='Required!', error_messages={'required': 'Sorry, you need to enter a valid email!'})
    password1 = forms.CharField(label='Enter your password', min_length=4, max_length=50, help_text='Required!', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Enter your password again', min_length=4, max_length=50, help_text='Required!', widget=forms.PasswordInput)
