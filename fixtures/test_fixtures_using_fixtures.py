import pytest

# fixtures/test_fixtures_using_fixtures.py
@pytest.fixture
def answer():
    return 42

@pytest.fixture
def half_the_answer(answer):
    return answer / 2

def test_answer(answer):
    assert answer == 42

def test_half_the_answer(half_the_answer):
    assert half_the_answer == 21
