def add(a, b):
    return a + b


def test_add():
    assert round(add(.1, .2),4) == .3
    assert add('space', 'ship') == 'spaceship'
