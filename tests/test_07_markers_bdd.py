import allure
import pytest


@allure.feature("Authorization")
@allure.story("Valid credentials")
@pytest.mark.parametrize("x", [True, 1])
def test_auth_valid(x):
    assert x


@allure.feature("Authorization")
@allure.story("Invalid credentials")
@pytest.mark.parametrize("x", [True, 0])
def test_auth_non_valid(x):
    assert x
