from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket
from decouple import config

import stripe


# Create your views here.

@login_required
def BasketView(request):
    basket= Basket(request)
    basket_total = str(basket.get_total_price())
    total = basket_total.replace('.', '')
    total = int(total)

    stripe.api_key = config('STRIPE_API_KEY')
    intent = stripe.PaymentIntent.create(
        amount = total,
        currency = 'eur',
        metadata={'user_id': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret':intent.client_secret})
