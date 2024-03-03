import time

def func(x):
    return x + 1

class TestClassSourceB:
    def test_fast(self):
        time.sleep(0.7)
        assert func(4) == 5

    # FAIL
    def test_slow_fail(self):
        time.sleep(1.7)
        assert func(3) == 5

    def test_medium(self):
        time.sleep(1.2)
        assert func(4) == 5