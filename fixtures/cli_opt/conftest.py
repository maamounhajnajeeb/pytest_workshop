import pytest

# fixtures/cli_opt/conftest.py
def pytest_addoption(parser):
    parser.addoption("--server-ip", type=str)

@pytest.fixture
def server_ip(request):
    return request.config.option.server_ip
