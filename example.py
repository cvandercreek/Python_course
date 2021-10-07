def add(a, b):
    return a + b


def test_add():
    assert round(add(.1, .2),4) == .3
    assert add('space', 'ship') == 'spaceship'
    
def subtract(a, b):
    return a - b  # <--- fix this 


# uncomment the following test
def test_subtract():
    assert subtract(2, 3) == -1
