class Basket():
    """
    A base Basket class, providing some default behaviours that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('basket-session-key')

        if 'basket-session-key' not in request.session:
            basket = self.session['basket-session-key'] = {}
        self.basket = basket

    def add(self, product, product_qty):
        """
        Adding and uploading the user basket session data
        """
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {'price':str(product.price), 'qty': int(product_qty)}

        self.session.modified = True

    
    def __len__(self):
        """
        Get the basket data and count the quentity of the items
        """
        return sum(item['qty'] for item in self.basket.values())