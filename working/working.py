import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d{1,2}:\d{2})\s(AM|PM)\sto\s(\d{1,2}:\d{2})\s(AM|PM)"
    match = re.match(pattern, s)
    if match:
        start_time_str, start_period, end_time_str, end_period = match.groups()
        start_hour, start_minute = map(int, start_time_str.split(":"))
        end_hour, end_minute = map(int, end_time_str.split(":"))

        if (
            start_hour < 1
            or start_hour > 12
            or start_minute < 0
            or start_minute > 59
            or end_hour < 1
            or end_hour > 12
            or end_minute < 0
            or end_minute > 59
        ):
            raise ValueError("Invalid time")

        if start_period == "AM" and start_hour == 12:
            start_hour = 0
        elif start_period == "PM" and start_hour != 12:
            start_hour += 12

        if end_period == "AM" and end_hour == 12:
            end_hour = 0
        elif end_period == "PM" and end_hour != 12:
            end_hour += 12

        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

    raise ValueError("Invalid format")


if __name__ == "__main__":
    main()