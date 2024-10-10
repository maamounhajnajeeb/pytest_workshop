import pytest

# fixtures/autouse/conftest.py
@pytest.fixture(autouse=True)
def tmp_homedir(tmp_path, monkeypatch):
    monkeypatch.setenv('HOME', str(tmp_path))
    return tmp_path
