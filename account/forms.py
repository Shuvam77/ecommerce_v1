from django import forms
from .models import UserBase


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required!')
    email = forms.EmailField(label='Enter Email', max_length=100, help_text='Required!', error_messages={'required': 'Sorry, you need to enter a valid email!'})
    password = forms.CharField(label='Enter your password', min_length=4, max_length=50, help_text='Required!', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Enter your password again', min_length=4, max_length=50, help_text='Required!', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email')

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        check_uname = UserBase.objects.filter(user_name=user_name)
        if check_uname.count():
            raise forms.ValidationError("Username already exists!")
        return user_name

    def clean_password2(self):
        cleanData = self.cleaned_data
        if cleanData['password'] != cleanData['password2']:
            raise forms.ValidationError("Your passwords doesnot matches!")
        return cleanData['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        check_email = UserBase.objects.filter(email=email)
        if check_email.exists():
            raise forms.ValidationError("Email already exists! Try other email address")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail Address'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Repeat Password'})