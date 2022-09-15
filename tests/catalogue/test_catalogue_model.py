import pytest

# Category Reverse


# Category __str__ Return
def test_store_model_category_str(product_category):
    assert product_category.__str__() == "django"
