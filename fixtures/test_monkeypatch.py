import os
import sys

# fixtures/test_monkeypatch.py
def func():
    path = os.environ.get("PATH", "")
    print(f"platform: {sys.platform}")
    print(f"PATH: {path}")

def test_one(monkeypatch):
    monkeypatch.setattr(sys, "platform", "MonkeyOS")
    monkeypatch.setenv("PATH", "/zoo")
    func()
    assert False

def test_two():
    func()
    assert False
