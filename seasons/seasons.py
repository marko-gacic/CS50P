import sys
import re
import inflect
p = inflect.engine()
from datetime import date



def main():
    day = birthday()
    minute = minutes(day)
    print((f'{sing(minute)} minutes').capitalize())


def birthday():
    birthday = input('Date of Birth: ')
    if match := re.search(r'^([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])$', birthday):
        return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    else:
        sys.exit('Invalid Date')


def minutes(day):
    birthday = day
    today = date.today()
    age = today - birthday
    if days := re.search(r'^([0-9]*) day', str(age)):
        minute = int(days.group(1)) * 24 * 60
        return(minute)


def sing(minute):
    words = p.number_to_words(minute, andword='')
    return(words)


if __name__ == "__main__":
    main()