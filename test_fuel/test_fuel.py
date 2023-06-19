from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()



def test_convert():
    assert convert("1/4") == 25
    try:
        convert("cat/dog")
    except ValueError:
        pass
    else:
        assert False
    try:
        convert("0/0")
    except ZeroDivisionError:
        pass
    else:
        assert False


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()