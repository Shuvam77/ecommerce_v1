from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import login, logout

from account.models import Customer, Address

from .forms import RegistrationForm, UserEditForm
from .token import account_activation_token

from django.contrib.auth.decorators import login_required

from orders.views import user_orders

# Create your views here.

@login_required
def dashboard(request):
    # orders = user_orders(request)
    return render(request, 'account/dashboard/dashboard.html')

def account_register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()

            #Setup Email
            current_site = get_current_site(request)
            subject = 'Activate Your Account!'
            message = render_to_string('account/registration/account_activation_email.html',{
            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),

            })
            user.email_user(subject=subject, message=message)
            return render(request, 'account/registration/register_email_confirm.html', {'form':registerForm})
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form':registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Customer.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')

@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance = request.user)
    return render(request, 'account/dashboard/edit_details.html', {'user_form':user_form})

@login_required
def delete_user(request, id):
    user = get_object_or_404(Customer,pk=id)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        logout(request)
        return redirect('account:delete_confirmation')
    return render (request, 'account/dashboard/delete_confirmation.html', {'user':user})

@login_required
def view_address(request):
    addresses = Address.objects.filter(customer=request.user)
    return render (request, "account/dashboard/addresses.html", {"addresses":addresses})

@login_required
def view_orders(request):
    orders = user_orders(request)
    return render(request, 'account/dashboard/orders.html', {'orders':orders})

