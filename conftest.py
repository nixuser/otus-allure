import allure
import pytest


@allure.step('step in conftest.py')
def conftest_step():
    pass


@pytest.fixture
def fixture_conftest_step():
    conftest_step()
