import pytest
from django.urls import reverse


# Category Reverse
def test_store_model_category_reverse(client, product_category):
    category = product_category
    url = reverse("store:category_list", args=[category.slug])
    response = client.get(url)
    assert response.status_code == 200


# Category __str__ Return
def test_store_model_category_str(product_category):
    assert product_category.__str__() == "django"


# ProductType __str__ Return
def test_store_model_productType_str(product_type_category):
    assert product_type_category.__str__() == "advance"


# ProductSpecification __str__ Return
def test_store_model_productSpec_str(product_specification_category):
    assert product_specification_category.__str__() == "volume-I"


# Product Reverse
def test_store_model_product_reverse(client, product_fact_category):
    # product = product_fact_category
    slug = "django_academy"
    url = reverse("store:product_detail", args=[slug])
    response = client.get(url)
    assert response.status_code == 200


# Product __str__ Return
def test_store_model_product_str(product_fact_category):
    assert product_fact_category.__str__() == "DjangoAcademy"
