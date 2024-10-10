import pytest
from hypothesis import given, strategies as st

# plugins/test_hypothesis_simple.py

@pytest.mark.parametrize('enc', ['utf-8', 'utf-16', 'ascii'])
@given(txt=st.text())
def test_encoding_round_trips(enc, txt):
    assert txt == txt.encode(enc).decode(enc)
