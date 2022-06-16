from importlib import import_module
from unittest import skip
from django.conf import settings
from django.http import HttpRequest

from django.test import TestCase, Client, RequestFactory

from django.contrib.auth.models import User
from django.urls import reverse
from store.models import Category, Product
from store.views import products_all


@skip("demonstrating skipping")
class TestSomethingSkips(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponse(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug= 'django')
        Product.objects.create(category_id=1, title='django for beginners', slug='django-for-beginners', created_by_id = 1, price='19.99', image= 'django')

    def test_homepage_url_allowed_host(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse("store:product_detail", args=['django-for-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse("store:category_list", args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()

        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()

        response = products_all(request)
        html = response.content.decode('utf8')
        # check to see data is correct
        # print(html)
        self.assertIn('<title>Home</title>', html)
        # self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)



    # def test_view_function(self):
    #     """
    #     Example: using request Factory
    #     """
    #     request = self.factory.get('/product/django-beginners')
    #     response = products_all(request)
    #     html = response.content.decode('utf8')
    #     self.assertIn('<title>Home</title>', html)
    #     self.assertEqual(response.status_code, 200)
