import pytest

# fixtures/test_yield_fixture.py

@pytest.fixture
def connected_client():
    client = Client()
    client.connect()
    yield client
    client.disconnect()

def test_client(connected_client):
    print("in the test")
