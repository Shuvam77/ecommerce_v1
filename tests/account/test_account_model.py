import pytest
from django.urls import reverse


def test_account_customer_str(customer_account):
    assert customer_account.__str__() == "admin@email.com"


def test_account_adminuser(admin_user):
    assert admin_user.__str__() == "adminuser@email.com"


def test_customer_email_on_input(customer_factory):
    # catch the exception
    with pytest.raises(ValueError) as e:
        email = customer_factory.create(email="")
    assert str(e.value) == "You must provide an email address!"


def test_customer_email_on_incorrect_input(customer_factory):
    # catch the exception
    with pytest.raises(ValueError) as e:
        email = customer_factory.create(email="a@com")
    assert str(e.value) == "You must provide a valid email address"


# def test_staff_not_true(customer_factory):
#     with pytest.raises(ValueError) as e:
#         staff = customer_factory.create(is_staff=False)
#     assert str(e.value) == "Superuser must be assigned to is_staff=True"
