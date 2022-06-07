class Basket():
    """
    A base Basket class, providing some default behaviours that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('basket-session-key')

        if 'basket-session-key' not in request.session:
            basket = self.session['basket-session-key'] = {'number': 757575757575}
        self.basket = basket