import pytest
from calculator.calculator import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 10) == 0


def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, 2) == -3
    with pytest.raises(ValueError):
        divide(1, 0)