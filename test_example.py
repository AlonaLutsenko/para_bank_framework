def add(a, b):
    return a + b

def test_add_function():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2
    assert add(5, -3) == 2
    assert add(0, 0) == 0

def test_add_with_floats():
    assert add(2.5, 3.5) == 6.0
    assert add(-1.5, 4.0) == 2.5