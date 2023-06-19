def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = d.replace('$', '').replace(',', '')
    try:
        return float(d)
    except ValueError:
        print("Invalid input")
        return 0.0


def percent_to_float(p):
    # TODO
    p = p.replace('%', '')
    try:
        return float(p) / 100
    except ValueError:
        print("Invalid input.")
        return 0.0

main()