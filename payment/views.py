import json
import os

import stripe
from basket.basket import Basket
from decouple import config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from orders.views import payment_confirmation

# Create your views here.


@login_required
def BasketView(request):
    basket = Basket(request)
    basket_total = str(basket.get_total_price())
    total = basket_total.replace(".", "")
    total = int(total)

    stripe.api_key = config("STRIPE_API_KEY")
    intent = stripe.PaymentIntent.create(amount=total, currency="eur", metadata={"user_id": request.user.id})

    return render(
        request,
        "payment/home.html",
        {"client_secret": intent.client_secret, "STRIPE_P_KEY": os.environ.get("STRIPE_P_KEY")},
    )


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == "payment_intent.succeeded":
        payment_confirmation(event.data.object.client_secret)

    else:
        print("Unhandled event type {}".format(event.type))
    return HttpResponse(status=200)


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, "payment/orderplaced.html")
