import factory
from faker import Faker
from store.models import Category, Product, ProductSpecification, ProductType

fake = Faker()

# Store factory fake data


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ("name", "slug")

    # category field name!
    name = "django"
    slug = "django"


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name = "advance"


class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecification
        django_get_or_create = ("name",)

    product_type = factory.SubFactory(ProductTypeFactory)
    name = "volume-I"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    product_type = factory.SubFactory(ProductTypeFactory)
    category = factory.SubFactory(CategoryFactory)
    title = "DjangoAcademy"
    description = fake.text()
    slug = "django_academy"
    regular_price = "29.99"
    discount_price = "19.99"
