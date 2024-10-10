import pytest

# marking/test_parametrization_marks.py

@pytest.mark.parametrize("arg1, arg2", [
    pytest.param(
        1, 1,
        marks=pytest.mark.xfail,
    ),
    (2, 3),
    (3, 4),
])
def test_xfail(arg1, arg2):
    assert arg2 == arg1 + 1
