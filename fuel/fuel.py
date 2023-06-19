def main():
    while True:
        fuel_fraction = input("Fraction: ").strip()
        percentage = fuel_percentage(fuel_fraction)
        if percentage is None:
            pass
        elif percentage == "E":
            print("E")
        elif percentage == "F":
            print("F")
        else:
            print(percentage)
            break



def fuel_percentage(fuel_fraction):
    try:
        x, y = map(int, fuel_fraction.split('/'))
        if y == 0 or x > y:
            return None

        percentage = (x / y) * 100
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return str(round(percentage)) + "%"

    except (ValueError, ZeroDivisionError):
        return None


main()
