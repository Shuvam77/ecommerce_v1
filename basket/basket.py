from decimal import Decimal
from itertools import product

from django.conf import settings
from store.models import Product
from decouple import config


class Basket():
    """
    A base Basket class, providing some default behaviours that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(config('BASKET_SESSION'))

        if config('BASKET_SESSION') not in request.session:
            basket = self.session[config('BASKET_SESSION')] = {}
        self.basket = basket


    def add(self, product, product_qty):
        """
        Adding and uploading the user basket session data
        """
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = product_qty
        else:
            self.basket[product_id] = {'price':str(product.regular_price), 'qty': int(product_qty)}
        self.save()

    
    def __len__(self):
        """
        Get the basket data and count the quentity of the items
        """
        return sum(item['qty'] for item in self.basket.values())

    
    def __iter__(self):
        """
        Collect the product_id in the session data to 
        query the database and return products.
        """
        product_chunks = self.basket.keys()
        products = Product.objects.filter(id__in=product_chunks)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product
        
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    def get_total_price(self):
        """
        Get the basket Total amount
        """
        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(11.50)
        total = subtotal + Decimal(shipping)
        return total

    def get_subtotal_price(self):
        """
        Get the sub Total amount
        """
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())


    def update(self, product, product_qty):
        """
        Update items from session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = product_qty
        self.save()


    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()


    def save(self):
        self.session.modified = True


    def clear(self):
        # del self.session[settings.BASKET_SESSION_ID]
        del self.session[config('BASKET_SESSION')]
        self.save()
