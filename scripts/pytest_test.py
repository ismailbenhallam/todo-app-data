import pytest


def divide(a: int, b: int):
    return a / b


def test_divide():
    assert divide(15, 3) == 5
    with pytest.raises(ZeroDivisionError):
        divide(7, 0)
