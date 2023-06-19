import subprocess

from numb3rs import validate


def test_valid_ip():
    assert validate("192.168.0.1") is True
    assert validate("10.0.0.0") is True
    assert validate("172.16.0.0") is True


def test_invalid_ip():
    assert validate("256.0.0.1") is False
    assert validate("192.168.0.256") is False
    assert validate("192.168.0") is False
    assert validate("192.168.0.1.2") is False
    assert validate("192.168.0.1.2.3") is False


def test_invalid_characters():
    assert validate("192.168.0.a") is False
    assert validate("192.168.0.$") is False
    assert validate("192.168.0.-1") is False


def test_empty_input():
    assert validate("") is False


def test_whitespace_input():
    assert validate("   ") is False


def test_different_separator():
    assert validate("192-168-0-1") is False
    assert validate("192_168_0_1") is False


def test_prefix_zero():
    assert validate("192.168.01.1") is False
    assert validate("192.168.001.1") is False


def test_max_min_values():
    assert validate("0.0.0.0") is True
    assert validate("255.255.255.255") is True
    assert validate("256.256.256.256") is False


def test_random_cases():
    assert validate("192.168.0.1 ") is False
    assert validate(" 192.168.0.1") is False
    assert validate("192. 168.0.1") is False


if __name__ == "__main__":
    tests = [
        test_valid_ip,
        test_invalid_ip,
        test_invalid_characters,
        test_empty_input,
        test_whitespace_input,
        test_different_separator,
        test_prefix_zero,
        test_max_min_values,
        test_random_cases,
    ]

    for test in tests:
        try:
            test()
            print(f"{test.__name__} passed")
        except AssertionError:
            print(f"{test.__name__} failed")

    completed_process = subprocess.run(["pytest", "test_numb3rs.py"], check=False)
    if completed_process.returncode == 0:
        print("All tests pass")
    else:
        raise SystemExit("Some tests failed")
