# basic/test_raises.py
import pytest

def divide(x, y):
    return x / y

def test_raises():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)
