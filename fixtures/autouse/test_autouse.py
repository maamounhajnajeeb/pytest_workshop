import pathlib

def test_empty():
    # verify tmp_homedir is active
    assert not list(pathlib.Path.home().iterdir())
