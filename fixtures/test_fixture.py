import pytest

# fixtures/test_fixture.py
@pytest.fixture
def answer():
    return 42

def test_universe(answer):
    assert answer == 42
