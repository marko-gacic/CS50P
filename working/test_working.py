import pytest
from working import convert


def test_convert_valid_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00")
    with pytest.raises(ValueError):
        convert("9:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM to 10:00 PM")
    with pytest.raises(ValueError):
        convert("9:61 AM")
    with pytest.raises(ValueError):
        convert("13:00 PM")


def test_convert_invalid_time():
    with pytest.raises(ValueError):
        convert("12:60 AM to 1:00 AM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 2:00 PM")
    with pytest.raises(ValueError):
        convert("0:00 PM to 1:00 PM")


def test_convert_overnight_hours():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("9:00 AM to 9:00 AM") == "09:00 to 09:00"
    assert convert("12:00 AM to 1:00 AM") == "00:00 to 01:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"
