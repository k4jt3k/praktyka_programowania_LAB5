import pytest
from binary_converter import decimal_to_binary


def test_conversion():
    """W zakresie"""
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(100) == "1100100"


def test_out_of_range():
    """Poza zakresem"""
    with pytest.raises(ValueError):
        decimal_to_binary(-1)
    with pytest.raises(ValueError):
        decimal_to_binary(101)


def test_not_natural_number():
    """Czesc dziesietna"""
    with pytest.raises(ValueError):
        decimal_to_binary(10.5)
