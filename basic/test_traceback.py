# basic/test_traceback.py

def divide(x, y):
    return x / y

def test_divide():
    assert divide(2, 0) == 0

def test_good():
    pass
