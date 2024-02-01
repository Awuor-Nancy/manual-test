import pytest
from add_two_numbers import add_two_numbers


def test_add_two_numbers_positive():
    result = add_two_numbers(5, 9)
    assert result == 14


def test_add_two_numbers_negative():
    result = add_two_numbers(-4, -3)
    assert result == -7


def test_add_two_numbers_zero():
    result = add_two_numbers(0, 0)
    assert result == 0


def test_add_two_numbers_float():
    result = add_two_numbers(3.5, 1.2)
    # Use approx for floating-point comparison
    assert result == pytest.approx(4.7)


def test_add_two_numbers_string():
    result = add_two_numbers("hello", "world")
    assert result == ("helloworld")
