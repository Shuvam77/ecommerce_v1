# conftest.py is where you setup test configurations and store the testcases that are used by test functions.
# The configurations and the testcases are called fixture in pytest.

import pytest


# Pytest fixtures have five different scopes: function, class, module, package, and session.
# The scope basically controls how often each fixture will be executed.
@pytest.fixture(scope="session")
def test_fixture2():
    print("Run on each session")
    return 1
