from bank import value

def main():
    test_with_hello()
    test_with_h()
    test_with_blank()


def test_with_hello():
    assert value("hello") == 0

def test_with_h():
    assert value("hi") == 20
    assert value("hole") == 20

def test_with_blank():
    assert value("") == 100


if __name__ == "__main__":
    main()