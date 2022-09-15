# conftest.py is where you setup test configurations and store the testcases that are used by test functions.
# The configurations and the testcases are called fixture in pytest.

import pytest
from pytest_factoryboy import register

from tests.factories import CategoryFactory


# Pytest fixtures have five different scopes: function, class, module, package, and session.
# The scope basically controls how often each fixture will be executed.
@pytest.fixture(scope="session")
def test_fixture2():
    print("Run on each session")
    return 1


register(CategoryFactory)
# This register is now accessable from category_factory namespace


@pytest.fixture
def product_category(db, category_factory):
    category = category_factory.create()
    return category
