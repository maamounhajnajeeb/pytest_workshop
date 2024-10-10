import pytest
import pathlib

# fixtures/test_usefixtures.py
@pytest.fixture
def tmp_homedir(tmp_path, monkeypatch):
    monkeypatch.setenv(
        'HOME', str(tmp_path))
    return tmp_path

@pytest.mark.usefixtures("tmp_homedir")
class TestHomeDir:
    def test_empty(self):
        # verify tmp_homedir is active
        homedir = pathlib.Path.home()
        assert not list(homedir.iterdir())
