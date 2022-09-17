import factory
from faker import Faker

from account.models import Address, Customer
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


# Account factory fake data
class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = "admin@email.com"
    name = "admin"
    mobile = "12345678912"
    password = "test@123"
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        # get model manager from customer
        manager = cls._get_manager(model_class)

        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    customer = factory.SubFactory(CustomerFactory)
    full_name = fake.name()
    phone = fake.phone_number()
    postcode = fake.postcode()
    address_line = fake.street_address()
    address_line2 = fake.street_address()
    town_city = fake.city_suffix()
