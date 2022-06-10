from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .basket import Basket
from store.models import Product

# Create your views here.


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket':basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_qty=product_qty)
        
        basket_qty = basket.__len__()
        response = JsonResponse({'qty':product_qty, 'basket_qty':basket_qty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        basket.delete(product = product_id)
        response = JsonResponse({'success':'Product Deleted!'})
        return response