import um


def test_count_single_um():
    assert um.count("um, hello, um, world") == 2


def test_count_multiple_um():
    assert um.count("um...") == 1


def test_count_no_um():
    assert um.count("yum") == 0


def test_count_empty_text():
    assert um.count("") == 0


def test_count_case_sensitive():
    assert um.count("uM, Um, UM") == 3


if __name__ == "__main__":
    test_count_single_um()
    test_count_multiple_um()
    test_count_no_um()
    test_count_empty_text()
    test_count_case_sensitive()
