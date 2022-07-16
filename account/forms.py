from django import forms
from .models import Customer, Address
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required!')
    email = forms.EmailField(label='Enter Email', max_length=100, help_text='Required!', error_messages={'required': 'Sorry, you need to enter a valid email!'})
    password = forms.CharField(label='Enter your password', min_length=4, max_length=50, help_text='Required!', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Enter your password again', min_length=4, max_length=50, help_text='Required!', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('user_name', 'email')

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        check_uname = Customer.objects.filter(user_name=user_name)
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
        check_email = Customer.objects.filter(email=email)
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
        model = Customer
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
        user = Customer.objects.filter(email=email)
        if not user:
            raise forms.ValidationError('Unfortunately we cannot find that email address!')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class':'form-control mb-3', 'placeholder':'Type New Password', 'id':'form-newpass'}
    ))
    new_password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput(
        attrs={'class':'form-control mb-3', 'placeholder':'Type New Password Again', 'id':'form-new-pass2'}
    ))

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["full_name", "phone", "address_line", "address_line2", "town_city", "postcode"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["full_name"].widget.attrs.update(
                {"class":"form-control mb-2 account-form", "placeholder":"Full Name"}
            )
            self.fields["phone"].widget.attrs.update(
                {"class":"form-control mb-2 account-form", "placeholder":"Phone"}
            )
            self.fields["address_line"].widget.attrs.update(
                {"class":"form-control mb-2 account-form", "placeholder": "Address Line1"}
            )
            self.fields["address_line2"].widget.attrs.update(
                {"class":"form-control mb-2 account-form", "placeholder": "Address Line2"}
            )
            self.fields["town_city"].widget.attrs.update(
                {"class":"form-control mb-2 account-form", "placeholder": "Town/City"}
            )
            self.fields["postcode"].widget.attrs.update(
                {"class":"form-control mb-2 account-form", "placeholder": "Postcode"}
            )