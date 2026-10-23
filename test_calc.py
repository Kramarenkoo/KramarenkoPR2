from calc import add, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    from calc import mul
    assert mul(3, 4) == 12


def test_add_negative():
    assert add(-2, -3) == -5
