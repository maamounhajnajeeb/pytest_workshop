import pytest

class Client:
    def connect(self):
        print("connect")

    def disconnect(self):
        print("disconnect")

# fixtures/test_fixture_finalizer.py
@pytest.fixture
def client(request):
    client = Client()
    request.addfinalizer(client.disconnect)
    return client

def test_one(client):
    pass

def test_two(client):
    pass

def test_three(client):
    pass
