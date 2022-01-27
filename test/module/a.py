import pytest


@pytest.fixture()
def number():
    return 9

def func(x):
    return x + 1


def test_answer(number):
    assert func(number) == 10
