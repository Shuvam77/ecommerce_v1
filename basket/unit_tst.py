from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from store.models import Category, Product


# Create your tests here.


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug= 'django')
        Product.objects.create(category_id=1, title='django for beginners', slug='django-for-beginners', created_by_id = 1, price='19.99', image= 'djangoB')
        Product.objects.create(category_id=1, title='django for intermediate', slug='django-for-intermediate', created_by_id = 1, price='29.99', image= 'djangoI')
        Product.objects.create(category_id=1, title='django for advance', slug='django-for-advance', created_by_id = 1, price='49.99', image= 'djangoA')

        self.client.post(
            reverse('basket:basket_add'), {"product_id":1, "product_qty":5, "action":"post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"product_id":2, "product_qty":7, "action":"post"}, xhr=True)
        
    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Testing adding items to the basket
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"product_id":3, "product_qty":10, "action":"post"}, xhr=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'qty':22, 'basket_total':'809.78'})

    def test_basket_delete(self):
        """
        Testing deleting items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_delete'), {"product_id":3, "action":"post"}, xhr=True)
        self.assertEqual(response.json(), {'qty':12, 'basket_total':'309.88'})

    def test_basket_update(self):
        """
        Testing updating items in the basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"product_id":2, "product_qty":5, "action":"post"}, xhr=True)
        self.assertEqual(response.json(), {'qty':10, 'basket_total':'249.90'})