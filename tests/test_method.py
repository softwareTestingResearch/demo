import time

def func(x):
    return x + 1

def test_slow():
    time.sleep(1.5)
    assert func(4) == 5

# FAIL
def test_fast_fail():
    time.sleep(0.5)
    assert func(3) == 5

def test_medium():
    time.sleep(1)
    assert func(4) == 5