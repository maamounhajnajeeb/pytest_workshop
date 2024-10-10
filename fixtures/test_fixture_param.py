import pytest

# fixtures/test_fixture_param.py

class MariaDB: ...
class Postgres: ...

@pytest.fixture(params=[
    MariaDB,
    Postgres,
])
def db(request):
    return request.param()

def test_init(db):
    assert False, db
