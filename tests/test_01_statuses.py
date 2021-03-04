import pytest
import random
import time


def test_success():
    """this test succeeds"""
    time.sleep(random.randint(0, 3))
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('bye-bye')


def test_outdated():
    with open('not_found') as f:
        f.readline()
