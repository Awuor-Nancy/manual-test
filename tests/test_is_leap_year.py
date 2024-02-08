import pytest
from leap_year import is_leap_year


def test_leap_year_multiple_of_4_not_100():
    assert is_leap_year(2024) is True
    assert is_leap_year(2028) is True


def test_leap_year_multiple_of_100_not_400():
    assert is_leap_year(1900) is False
    assert is_leap_year(2100) is False


def test_leap_year_multiple_of_400():
    assert is_leap_year(2000) is True
    assert is_leap_year(2400) is True


def test_leap_year_not_multiple_of_4():
    assert is_leap_year(2023) is False
    assert is_leap_year(2025) is False


def test_negative_year():
    with pytest.raises(ValueError):
        is_leap_year(-1)


def test_zero_year():
    with pytest.raises(ValueError):
        is_leap_year(0)
