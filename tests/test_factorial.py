import pytest
from factorial import factorial


def test_factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def test_factorial_of_zero():
    assert factorial(0) == 1


def test_factorial_of_positive_number():
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(7) == 5040


def test_factorial_of_negative_number():
    with pytest.raises(ValueError):
        factorial(-3)
