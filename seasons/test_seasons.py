from datetime import date
from seasons import calculate_age_in_minutes, print_age_in_minutes, parse_date


def test_calculate_age_in_minutes():
    birthdate = date(1999, 1, 1)
    assert calculate_age_in_minutes(birthdate) == 525600

    birthdate = date(1999, 12, 31)
    assert calculate_age_in_minutes(birthdate) == 1440

    birthdate = date(1970, 1, 1)
    assert calculate_age_in_minutes(birthdate) == 15778080


def test_parse_date():
    date_str = "1999-01-01"
    assert parse_date(date_str) == date(1999, 1, 1)

    date_str = "2000-12-31"
    assert parse_date(date_str) == date(2000, 12, 31)


def test_print_age_in_minutes(capsys):
    minutes = 525600
    print_age_in_minutes(minutes)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Five hundred twenty-five thousand, six hundred minutes"

    minutes = 1440
    print_age_in_minutes(minutes)
    captured = capsys.readouterr()
    assert captured.out.strip() == "One thousand four hundred, forty minutes"

    minutes = 15778080
    print_age_in_minutes(minutes)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fifteen million seven hundred, seventy-eight thousand, eighty minutes"
