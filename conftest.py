import allure
import os
import pytest


@allure.step('step in conftest.py')
def conftest_step():
    pass


@pytest.fixture
def fixture_conftest_step():
    conftest_step()


@pytest.fixture(scope="session", autouse=True)
def get_environment(pytestconfig):
    props = {
        'Shell': os.getenv('SHELL'),
        'Terminal': os.getenv('TERM'),
        'Stand': 'Production'
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/allure-results/environment.properties', 'w') as f:
        for k, v in props.items():
            f.write(f'{k}={v}\n')
