from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar = Jar(20)
    assert jar.capacity == 20

    try:
        jar = Jar(-5)
        assert False  # Should not reach this point
    except ValueError:
        assert True  # Expected ValueError


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    assert jar.size == 3

    try:
        jar.deposit(4)
        assert False  # Should not reach this point
    except ValueError:
        assert True  # Expected ValueError

    assert str(jar) == "🍪🍪🍪"
    assert jar.size == 3


def test_withdraw():
    jar = Jar(5)

    jar.deposit(3)
    jar.withdraw(2)
    assert str(jar) == "🍪"
    assert jar.size == 1

    try:
        jar.withdraw(2)
        assert False  # Should not reach this point
    except ValueError:
        assert True  # Expected ValueError

    assert str(jar) == "🍪"
    assert jar.size == 1


def test_empty():
    jar = Jar(10)

    assert str(jar) == ""
    assert jar.size == 0

    try:
        jar.withdraw(1)
        assert False  # Should not reach this point
    except ValueError:
        assert True  # Expected ValueError

    assert str(jar) == ""
    assert jar.size == 0


def test_exceed_capacity():
    jar = Jar(3)

    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    assert jar.size == 2

    try:
        jar.deposit(2)
        assert False  # Should not reach this point
    except ValueError:
        assert True  # Expected ValueError

    assert str(jar) == "🍪🍪"
    assert jar.size == 2


def test_withdraw_all():
    jar = Jar(5)

    jar.deposit(3)
    jar.withdraw(3)
    assert str(jar) == ""
    assert jar.size == 0


def test_multiple_operations():
    jar = Jar(5)

    jar.deposit(2)
    jar.withdraw(1)
    jar.deposit(3)
    jar.withdraw(2)
    assert str(jar) == "🍪"
    assert jar.size == 1
