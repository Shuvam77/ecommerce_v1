import factory
from faker import Faker
from store.models import Category

fake = Faker()

# Store factory fake data


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # category field name!
    name = "django"
    slug = "django"
