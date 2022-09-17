import pytest

from account.forms import RegistrationForm, UserAddressForm


@pytest.mark.parametrize(
    "full_name, phone, address_line, address_line2, town_city, postcode, validity",
    [
        ("taylor", "02343343434", "add1", "add2", "town", "postcode", True),
        ("", "02343343434", "add3", "add6", "town2", "postcode2", False),
    ],
)
def test_customer_address(full_name, phone, address_line, address_line2, town_city, postcode, validity):
    form = UserAddressForm(
        data={
            "full_name": full_name,
            "phone": phone,
            "address_line": address_line,
            "address_line2": address_line2,
            "town_city": town_city,
            "postcode": postcode,
        }
    )

    assert form.is_valid() is validity


def test_customer_create_address(client, customer_account):
    user = customer_account
    client.force_login(user)
    response = client.post(
        "/account/add_address/",
        data={
            "full_name": "admin",
            "phone": "0548695364",
            "address_line": "here",
            "address_line2": "there",
            "town_city": "anywhere",
            "postcode": "56072",
        },
    )
    assert response.status_code == 302


@pytest.mark.parametrize(
    "user_name, email, password, password2, validity",
    [
        ("user1", "admin@admin.com", "12345a", "12345a", True),
        ("user1", "admin@admin.com", "12345a", "", False),
        ("user1", "admin@admin.com", "12345a", "12345b", False),
        ("user1", "admin@.com", "12345a", "12345a", False),
    ],
)
@pytest.mark.django_db
def test_create_account(user_name, email, password, password2, validity):
    form = RegistrationForm(
        data={
            "user_name": user_name,
            "email": email,
            "password": password,
            "password2": password2,
        }
    )
    assert form.is_valid() is validity


# Account create view
@pytest.mark.parametrize(
    "user_name, email, password, password2, validity",
    [
        ("user1", "admin@admin.com", "12345a", "12345a", 200),
        ("user1", "admin@admin.com", "12345a", "12345b", 400),
        ("user1", "", "12345a", "12345a", 400),
    ],
)
@pytest.mark.django_db
def test_create_account_view(client, user_name, email, password, password2, validity):
    response = client.post(
        "/account/",
        data={
            "user_name": user_name,
            "email": email,
            "password": password,
            "password2": password2,
        },
    )
    assert response.status_code == validity


def test_account_register_redirect(client, customer_account):
    user = customer_account
    client.force_login(user)
    response = client.get("/account/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_account_register_render(client):
    response = client.get("/account/")
    assert response.status_code == 200
