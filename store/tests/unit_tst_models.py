from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        """
        Test category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return(self):
        """
        Testo category model return!
        """
        data = self.data1
        self.assertEquals(str(data), 'django')



class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug= 'django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django for beginners', slug='django-for-beginners', created_by_id = 1, price='19.99', image= 'django')

    def test_product_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))

    def test_product_model_return(self):
        """
        Testo product model return!
        """
        data = self.data1
        self.assertEquals(str(data), 'django for beginners')