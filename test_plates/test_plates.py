from plates import is_valid

def main():
    test_valid()
    test_invalid()


def test_valid():
    assert is_valid("HELLO") == True
    assert is_valid("CS50") == True

def test_invalid():
    assert is_valid("GOODBYE") == False
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("CS50P") == False
    assert is_valid("50") == False

if __name__ == "__main__":
    main()