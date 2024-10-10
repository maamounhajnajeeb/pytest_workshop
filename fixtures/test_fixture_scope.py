import time, pytest
# fixtures/test_fixture_scope.py

@pytest.fixture(scope="function")
def answers():
    time.sleep(2)
    return [42]

def test_one(answers):
    assert answers == [42]

def test_two(answers):
    assert answers == [42]
