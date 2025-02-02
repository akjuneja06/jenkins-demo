from calculator import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(5,6) == 11

def test_sub():
    assert sub(5,1) == 4
    assert sub(7,2) == 5
