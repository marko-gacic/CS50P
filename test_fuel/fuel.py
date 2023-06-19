def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        result = gauge(percentage)
        print(result)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")



def convert(fraction):
    x, y = map(int, fraction.split('/'))

    if not (isinstance(x, int) and isinstance(x, int)):
        raise ValueError("X and Y must be integers")
    if x > y:
        raise ValueError("X must be less or equal to Y")
    if y == 0:
        raise ZeroDivisionError("Y must not be zero")

    percentage = round((x / y) * 100)

    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

