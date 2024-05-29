def add(a,b):
    return a + b
def test_add():
    assert add(100,200) == 300
    assert add(100,-100) == 0
