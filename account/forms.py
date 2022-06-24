from logging import PlaceHolder
from django import forms
from .models import UserBase
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


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


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email Address', 'id':'login-username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control mb-3', 'placeholder':'Password', 'id':'login-pwd'}
    ))


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='Account Email cannot be changed', max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email Address', 'id':'form-email', 'readonly':'readonly'}))
    # user_name = forms.CharField(label='Username', min_length=4, max_length=50, widget=forms.TextInput(
    #     attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-username', 'readonly': 'readonly'}))
    first_name = forms.CharField(label='FirstName', min_length=4, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    about = forms.CharField(label='About User', min_length=20, max_length=150, widget=forms.Textarea(
        attrs={'class': 'form-control mb-3', 'placeholder': 'User Bio', 'id': 'form-bio'}))

    class Meta:
        model = UserBase
        fields = ('email', 'first_name', 'about')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user_name'].required = True
        self.fields['email'].required = True


class PwdResetForm(PasswordResetForm):
    
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class':'form-control mb-3', 'placeholder': 'Email', 'id':'form-email'}
    ))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = UserBase.objects.filter(email=email)
        if not user:
            raise forms.ValidationError('Unfortunately we cannot find that email address!')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control mb-3', 'placeholder':'Type New Password', 'id':'reset-pwd1'}
    ))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control mb-3', 'placeholder':'Type New Password Again', 'id':'reset-pwd2'}
    ))