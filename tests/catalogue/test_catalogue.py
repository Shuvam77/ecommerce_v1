# from django.test import TestCase

import pytest

# class TestClass(TestCase):
#     def test_runserver(self):
#         self.assertEqual("Hello", "Hello")


# @pytest.fixture(scope="module")
# def test_fixture1():
#     print("Run each test")
#     return 1


def test_hello_world(test_fixture2):
    print("function_fixture1")
    assert test_fixture2 == 1


# Mark test will fail
@pytest.mark.xfail
def test_hello_world2(test_fixture2):
    print("function_fixture2")
    assert test_fixture2 == 2


# Mark test skip
@pytest.mark.skip
def test_hello_world2(test_fixture2):
    print("function_fixture3")
    assert test_fixture2 == 1
