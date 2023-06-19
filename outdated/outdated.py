MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def prompt_for_date():
    while True:
        date_input = input("Enter a date (in month-day-year format): ")
        try:
            month, day, year = map(int, date_input.split("/"))
            if validate_date(day, month, year):
                iso_date = format_date_iso(year, month, day)
                return iso_date
            else:
                print("Invalid date. Please try again.")
        except ValueError:
            try:
                month_str, day_str, year_str = date_input.split()
                month = MONTHS.index(month_str) + 1
                day = int(day_str.strip(","))
                year = int(year_str)
                if validate_date(day, month, year):
                    iso_date = format_date_iso(year, month, day)
                    return iso_date
                else:
                    print("Invalid date. Please try again.")
            except ValueError:
                print("Invalid date format. Please try again.")

def validate_date(day, month, year):

    if month < 1 or month > 12:
        return False


    if day < 1 or day > 31:
        return False

    if year < 1:
        return False

    return True

def format_date_iso(year, month, day):
    return f"{year:04}-{month:02}-{day:02}"

def main():
    iso_date = prompt_for_date()
    print(iso_date)

if __name__ == "__main__":
    main()
