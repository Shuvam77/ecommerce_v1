from django.shortcuts import render
from django.http.response import JsonResponse

from basket.basket import Basket
from .models import Order, OderItem

# Create your views here.

def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        user_id = request.user.id
        order_key = request.POST.get('order_key')
        baskettotal = basket.get_total_price()
        
        custName = request.POST.get('custName')
        custAdd = request.POST.get('custAdd')
        custAdd2 = request.POST.get('custAdd2')
        postCode = request.POST.get('postCode')

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name=custName, address1=custAdd, address2=custAdd2, post_code=postCode, total_paid=baskettotal, order_key=order_key)
            order_id = order.pk
            for item in basket:
                OderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])
        response = JsonResponse({'success': 'Order Saved!'})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders





# Something of add later on!!
        # custName = request.POST.get('custName')
        # custAdd = request.POST.get('custAdd')
        # custAdd2 = request.POST.get('custAdd')
        # postCode = request.POST.get('postCode')

        # order = Order.objects.create(user_id=user_id, full_name=custName, address1=custAdd, address2=custAdd2, post_code=postCode, total_paid=baskettotal, order_key=order_key)
